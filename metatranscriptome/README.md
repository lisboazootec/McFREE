#1. Pre-processamento das sequências
## 1.1 FastQjoin
### 1.1.1 FastQJoin - overlap *{s0210}*
Unir sequencias foward e reverse que podem ser pareadas por overlap.

__Programa__ [EA-Utils/FastQJoin](https://github.com/ExpressionAnalysis/ea-utils.git)

### 1.1.2 FastQJoin - convert to fasta
Converte o arquivo `fastq` para `fasta`.

__Programa__ [SeqKit](https://github.com/shenwei356/seqkit)
_Subcomnando_ `fq2fa`

### 1.1.3 FastQJoin - concat unpairs *{s0220}*
Concatena as sequências não pareadas pelo passo anterior.
__Programa__ [SeqKit](https://github.com/shenwei356/seqkit)
_Subcomnando_ `concat`

### 1.1.4 FastQJoin - final
Concatena os arquivos dos passos 1.1.2 e 1.1.3 em um só. 
__Comando__ `cat` ou similar

## 1.2 FastUniq - remove duplicates  *{s0230}*
Remove as sequencias duplicadas e salva em um arquivo separado para integração futura.

__Programa__ [SeqKit](https://github.com/shenwei356/seqkit)
_Subcomnando_ `rmdup`

# 2. Megablast
# 2.1 Database download
Realiza o download das base de dados de referência para o alinhamento das sequências.

__Programa__ [NCBI Genome Downloading Scripts](https://github.com/kblin/ncbi-genome-download)
_Bases_ `fungi`, `bacteria` e `viral`

# 2.2 Megablast *{s0240}*
Executa o algoritmo de alinhamento das sequencias da amostra contra as bases de referências.

__Programa__ [HS-BLASTn](https://github.com/chenying2016/queries)

