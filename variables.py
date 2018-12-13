from utils import *


files = {

	# root folders
	'root':'pipeline',
	
	'lib':'{root}/lib', # Contém todos os programas utilizados na pipeline
	'lib_fastQJoin':'{lib}/ExpressionAnalysis'
	
	'data':'{root}/data', # Contém todos os arquivos de dados utilizados na pipeline
	'data_fastQJoin':'{data}/FastQJoin'
	'metaseq':'{data}/Metatranscriptome_sequences', # Contém os arquivos de sequencias brutas
	'databases':'{data}/Databases',
	
	'trinity':'{lib}/Trinity',

	#### INPUT FILES

	'fSeqFastQ':'{metaseq}/F.fastq', # Sequência forward bruta gerado pelo sequenciamento
	'rSeqFastQ':'{metaseq}/R.fastq', # Sequência reverse bruta gerado pelo sequenciamento
	'accession_TaxId':'{databases}/accession2taxid.filterd.tsv', # Relacionamento de Accesion Number e Tax ID
	'mergedFastQ':'{data_fastQJoin}/merged.fastq',
	'unpared1_fastq':'{data_fastQJoin}/unpared1.fastq'.
	'unpared2_fastq':'{data_fastQJoin}/unpared2.fastq',
	'final_fastq':'{data_fastQJoin}/final.fastq',

	'proteinACC_Accession':'{databases}/proteinacc2acession.tsv', # ?
	'nomReduant_diamond':'{databases}/nr_dmnd.db', # Dados de proteínas não redundantes do NCBI no formato para o Diamond
	'nomReduant_kegg':'{databases}/nr_kegg.db', # Relacionamento de proteínas não redundantes do NCBI com o KEGG Ortológico

	#### OUTPUT FILES

	#### CUSTOM ARGS

	'cpu_limit':'64',
	'memory_limit':'200',


}

files = {
}

runners = {
}