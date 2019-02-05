from utils import *


files = {

	# root folders
	'root':'pipeline',
	
	'lib':'{root}/lib', # Contém todos os programas utilizados na pipeline
	'lib_fastQJoin':'{lib}/ExpressionAnalysis'
	
	'data':'{root}/data', # Contém todos os arquivos de dados utilizados na pipeline
	'data_fastQJoin':'{data}/FastQJoin'
	'data_fastQuniq':'{data}/FastQUniq'
	'metaseq':'{data}/Metatranscriptome_sequences', # Contém os arquivos de sequencias brutas
	'databases':'{data}/Databases',
	'data_HSBLASTn':'{data}/HSBLASTn'
	'data_Trinity':'{data}/Trinity'
	'data_TransDecoder':'{data}/TransDecoder'
	'lib_trinity':'{lib}/Trinity',
	'lib_lca':'{lib}/LCA',
	'lib_transDecoder':'{lib}/TransDecoder'

	#### INPUT FILES

	'fSeqFastQ':'{metaseq}/F.fastq', # Sequência forward bruta gerado pelo sequenciamento
	'rSeqFastQ':'{metaseq}/R.fastq', # Sequência reverse bruta gerado pelo sequenciamento
	'accession_TaxId':'{databases}/accession2taxid.filterd.tsv', # Relacionamento de Accesion Number e Tax ID
	'mergedFastQ':'{data_fastQJoin}/merged.fastq',
	'unpared1_fastq':'{data_fastQJoin}/unpared1.fastq'.
	'unpared2_fastq':'{data_fastQJoin}/unpared2.fastq',
	'grouped_fastq':'{data_fastQJoin}/grouped.fastq',

	'proteinACC_Accession':'{databases}/proteinacc2acession.tsv', # ?
	'nomReduant_diamond':'{databases}/nr_dmnd.db', # Dados de proteínas não redundantes do NCBI no formato para o Diamond
	'nomReduant_kegg':'{databases}/nr_kegg.db', # Relacionamento de proteínas não redundantes do NCBI com o KEGG Ortológico
	
	'list_redudants':'{data_fastQuniq}/list_redudants.json',
	'uniq_fastq':'{data_fastQJoin}/uniq.fastq',
	'refseq_fna':'{databases}/refseq.fna', # 
	'refseq_fna_counts_obinary':'{databases}/refseq.fna.counts.obinary', # 
	'blastn_fa':'{data_HSBLASTn}/blastn.fa',
	'trinity_fa':'{data_Trinity}/Trinity.fasta', 
	'trinity_fa':'{data_Trinity}/Trinity.fasta', 
	'longestOrfs':'{data_TransDecoder}/longest_orfs.pep'

	#### OUTPUT FILES

	#### CUSTOM ARGS

	'cpu_limit':'64',
	'memory_limit':'200',
	'max_cov': '5' #deve ser modificado


}

steps = [
	{
		"name": "Junta as reads reverse e forward",
		'index':"s0210",
		'runner':'fastQJoin',
		'args':'-p {cpu_limit} -m {memory_limit} {fSeqFastQ} {rSeqFastQ} -o {mergedFastQ}',
		'outputs':['{unpared1_fastq}','{unpared2_fastq}'],
 		"description": "--",
	},
	{
		"name": "Juntar as reads não unidas",
		'index':"s0220",
		'runner':'fastQJoinRemains',
		'args':'--unpared1-file {unpared1_fastq} --unpared2-file {unpared2_fastq} --merged-file {mergedFastQ} --output-file {grouped_fastq}',
		'outputs':[]
	},{
		"name": "Retirar as sequencias redundantes",
		'index':"s0230",
		'runner':'fastqUniqSeq',
		'args':'--redundant-file {grouped_fastq} --output-file {uniq_fastq}',
		'outputs':['{list_redudants}']
	},{
		"name": "MegaBLAST",
		'index':"s0240",
		'runner':'HSBLASTn',
		'args':'-db {refseq_fna} -window_masker_db {refseq_fna_counts_obinary} -query {uniq_fastq} -out {blastn_fa} -outfmt 7',
		'outputs':[]
	},{
		"name": "Lowest Commumn Ancestor",
		'index':"s0250",
		'runner':'lca',
		'args': #temos de rever os argumentos
		'outputs':[]
	},{
		"name": "Contig Assembly (Trinity)",
		'index':"s0260",
		'runner':'trinity',
		'args':'--seqType fq --SS_lib_type FR --normalize_max_read_cov {max_cov} --left {fSeqFastQ} --right {rSeqFastQ} --CPU {cpu_limit} --output {trinity_fa} --trimmomatic "ILLUMINACLIP:$TRIMMOMATIC_DIR/adapters/TruSeq3-PE.fa:2:30:10 HEADCROP:10 CROP:285 LEADING:10 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:25"',
 		"description": "Inicio da análise funcional",
		'outputs':[]
	},{
		"name": "Identificação CDS",
		'index':"s0270",
		'runner':'transDecoder',
		'args':'-t {trinity_fa} -m {memory_limit}',
		'outputs':['{longestOrfs}']
	},{
		"name": "Selecionando candidatos para treino/Buscando evidências de candidatos",
		'index':"s0280",
		'runner':'grep_sed_cut',
		'args':'grep "complete" {longestOrfs} | sed -e "s/>//g" | cut -d " " -f1 > {complete_candidates}',
		'outputs':[]
	},{
		"name": "",
		'index':"passo7c1",
		'runner':'makeblastdb',
		'args':"-dbtype 'prot' -in {longestOrfs} -parse_seqids -out {predicted}",
		'outputs':[]
	},{
		"name": "",
		'index':"passo7c2",
		'runner':'blastdbcmd',
		'args':"-db {predicted} -entry_batch {complete_candidates} > {complete_fasta}",
		'outputs':[]
	},{
		"name": "",
		'index':"passo7c2",
		'description':"sed -e 's/lcl|//g'",
		'runner':'replace_lcl',
		'args':"--input-file {complete_fasta} --output-file {complete_fasta}",
		'outputs':[]
	},{
		"name": "",
		'index':"passo7d1",
		'runner':'diamond',
		'args':'-d {nr_dmnd} -q {complete_fasta} -a {complete_blastp} -e 1e-6 -p 64 -f "6 qacc sacc pident qlen slen length qcovs evalue bitscore" -k 1',
		'outputs':[]
	},{
		"name": "",
		'index':"passo7d2",
		'runner':'diamond',
		'args':'view -a {complete_blastp_daa} -o {complete_blastp_m8}',
		'outputs':[]
	},{
		"name": "",
		'index':"passo7e1",
		'runner':'cat_cut_sort',
		'args':'{complete_blastp_m8} | cut -f1 | sort -u > {evidences_list}',
		'outputs':[]
	},{
		"name": "",
		'index':"passo7e2",
		'runner':'makeblastdb',
		'args':"-dbtype 'nucl' -in {longestOrfs} -parse_seqids -out {cds}",
		'outputs':[]
	},{
		"name": "",
		'index':"passo7e3",
		'runner':'blastdbcmd',
		'args':"-db {cds} -entry_batch {evidences_list} | sed -e 's/lcl|//g' > {train_fasta}",
		'outputs':[]
	},{
		"name": "",
		'index':"passo7f",
		'runner':'transDecoder',
		'args':"-t {trinity_fa} --cpu 4 --train train.fasta",
		'outputs':[]
	},{
		"name": "",
		'index':"passo7g1",
		'runner':'diamond',
		'args':'blastp -d {nr_dmnd} -q {trinity_fasta_transdecoder_pep} -a {final_blastp} -e 1e-6 -p 64 -f "6 qacc sacc pident qlen slen length qcovs evalue bitscore" -k 1',
		'outputs':[]
	},{
		"name": "",
		'index':"passo7g2",
		'runner':'diamond',
		'args':'view -a {final_blastp_daa} -o {final_blastp_m8}',
		'outputs':[]
	},{
		"name": "",
		'index':"passo8b",
		'runner':'star',
		'args':'--runMode genomeGenerate --runThreadN 64 --genomeDir {reference} --limitGenomeGenerateRAM=80000000000 --genomeFastaFiles {trinity_fasta_transdecoder_cds}',
		'outputs':[]
	},{
		"name": "",
		'index':"passo8c",
		'runner':'star',
		'args':'--runMode genomeGenerate --runThreadN 64 --genomeDir {reference} --readFilesIn {f_fastq} {f_fastq} --outFileNamePrefix {star_map} --outSAMtype BAM SortedByCoordinate',
		'outputs':[]
	},{
		"name": "",
		'index':"",
		'runner':'samtools',
		'args':"view {star_map_aligned} > {reads}",
		'outputs':[]
	},{
		"name": "",
		'index':"",
		'description':"cut -f1,3",
		'runner':'cut',
		'args':"--input-file {reads} --output-file {reads_id}",
		'outputs':[]
	},{
		"name": "",
		'index':"passo10",
		'runner':'script_groupko',
		'args':"{final_blastp_m8} {reads_id} {blastn_fa}",
		'outputs':[]
	},{
		"name": "",
		'index':"",
		'runner':'mysql',
		'args':"-h {db_hostname} -D {db_db} -u {db_user} -p < {query_sql} > {lib}.final.tsv",
		'outputs':[]
	}
]

runners = {
	'fastQJoin':'{lib_fastQJoin}/clipper/fastq-join', # 
	'fastQJoinRemains':fastq_join_remains,
	'fastqUniqSeq': fastq_uniq_seq
	'HSBLASTn':'HS-BLASTn',
	'lca':'{lib_lca}/lca.py',
	'trinity':'{lib_trinity}/[trinity_runner]',
	'transDecoder':'{lib_transDecoder}/TransDecoder.LongOrfs'
	'mapFilterLongestOrfs':mapfilter_longest_orfs
}