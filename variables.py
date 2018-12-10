from utils import *

steps = {	
	"passo_0100": ['{donwload_banco_de_dados}','{accession2taxid.filterd.tsv} {proteinacc2acession} {NR.dmnd}{NR.KEGG}'],
	"passo_0210": ['{programa_fastq_join}','-p 64 -m 200 {F.fastq} {R.fastq} -o {merged.fastq}'],
	"passo_0220": ['{script_fastq_join}','{unpared1.fastq} {unpared2.fastq} -unir* {merged.fastq} -o {final.fastq}'],
	"passo_0330": ['{script_fasuniq_join}','{final.fastq} -o {final_uniq.fastq} {repetition_list.json}'],
	"passo_0400": ['{programa_HS_BLASTn}','-db {refseq.fna} -window_masker_db {refseq.fna.counts.obinary} -query {final_uniq.fastq} -out {results.fa} -outfmt 7'],
	"passo_0600": ['{programa_trinity}','--seqType fq --SS_lib_type FR --normalize_max_read_cov 5 --left {F.fastq} --right {R.fastq} --CPU 64 --max_memory 50G --output  {Trinity.fasta} --trimmomatic "ILLUMINACLIP:$TRIMMOMATIC_DIR/adapters/TruSeq3-PE.fa:2:30:10 HEADCROP:10 CROP:285 LEADING:10 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:25"'],
	"passo_0720": ['{programa_TransDecoder.LongOrfs}','-t {Trinity.fasta}  -m 100'],
	"passo_0731": ['{programa_makeblastdb}','-dbtype "prot" -in {Trinity.fasta.transdecoder_dir_longest_orfs.pep} -parse_seqids -out {Predicted}'],
	"passo_0732": ['{programa_blastdbcmd}','-db {Predicted} -entry_batch {complete_candidates}'],
	"passo_0741": ['{programa_diamond}','-d {NR.dmnd} -q {complete.fasta} -a {complete.blastp} -e 1e-6 -p 64 -f "6 qacc sacc pident qlen slen length qcovs evalue bitscore" -k 1'],
	"passo_0742": ['{programa_diamond}','view -a {complete.blastp.daa} -o {complete.blastp.m8}'],
	"passo_07e2": ['{programa_makeblastdb}','-dbtype "nucl" -in {Trinity.fasta.transdecoder_dir_longest_orfs.cds} -parse_seqids -out {cds}'],
	"passo_07c3": ['{programa_blastdbcmd}','-db {cds} -entry_batch {evidences.list}'],
	"passo_0760": ['{programa_TransDecoder.LongOrfs}','-t {Trinity.fasta} --cpu 4 --train train.fasta'],
	"passo_0771": ['{programa_diamond}','blastp -d {NR.dmnd} -q {Trinity.fasta.transdecoder.pep} -a {final.blastp} -e 1e-6 -p 64 -f "6 qacc sacc pident qlen slen length qcovs evalue bitscore" -k 1'],
	"passo_0772": ['{programa_diamond}','view -a {final.blastp.daa} -o {final.blastp.m8}'],
	"passo_0820": ['{programa_STAR}','--runMode genomeGenerate --runThreadN 64 --genomeDir {reference} --limitGenomeGenerateRAM=80000000000 --genomeFastaFiles {Trinity.fasta.transdecoder.cds}'],
	"passo_0830": ['{programa_STAR}','--runMode genomeGenerate --runThreadN 64 --genomeDir {reference} --readFilesIn {F.fastq} {R.fastq} --outFileNamePrefix {STARMap} --outSAMtype BAM SortedByCoordinate'],
	"passo_0900": ['{programa_samtools}','view {STARMapAligned.sortedByCoord.out.bam}'],
	"passo_1000": ['{script_groupko.py}','{final.blastp.m8} {ReadsId.txt} {blastn.fa}'],
}

files = {
}

runners = {
}