
# Data
## Files
## Input
- `fSeqFastQ`:
	- **Path**: `{metaseq}/F.fastq`

- `rSeqFastQ`:
	- **Path**: `{metaseq}/R.fastq`

- `accession_TaxId`:
	- **Path**: `{databases}/accession2taxid.filterd.tsv`

- `mergedFastQ`:
	- **Path**: `{data_fastQJoin}/merged.fastq`

- `unpared1_fastq`:
	- **Path**: `{data_fastQJoin}/unpared1.fastq`

- `unpared2_fastq`:
	- **Path**: `{data_fastQJoin}/unpared2.fastq`

- `grouped_fastq`:
	- **Path**: `{data_fastQJoin}/grouped.fastq`

- `proteinACC_Accession`:
	- **Path**: `{databases}/proteinacc2acession.tsv`

- `nomReduant_diamond`:
	- **Path**: `{databases}/nr_dmnd.db`

- `nomReduant_kegg`:
	- **Path**: `{databases}/nr_kegg.db`

- `list_redudants`:
	- **Path**: `{data_fastQuniq}/list_redudants.json`

- `uniq_fastq`:
	- **Path**: `{data_fastQJoin}/uniq.fastq`

- `refseq_fna`:
	- **Path**: `{databases}/refseq.fna`

- `refseq_fna_counts_obinary`:
	- **Path**: `{databases}/refseq.fna.counts.obinary`

- `blastn_fa`:
	- **Path**: `{data_HSBLASTn}/blastn.fa`

- `trinity_fa`:
	- **Path**: `{data_Trinity}/Trinity.fasta`

- `longestOrfs`:
	- **Path**: `{data_TransDecoder}/longest_orfs.pep`


#Steps

| **Key**:         | *s0210*                            |
| ---------------- | ---------------------------------- |
| **Name**:        | *Junta as reads reverse e forward* |
| **Description**: | *--*                               |


  - **Key**: *s0220*
  - **Name**: *Juntar as reads não unidas*
  - **Description**: **

  - **Key**: *s0230*
  - **Name**: *Retirar as sequencias redundantes*
  - **Description**: **

  - **Key**: *s0240*
  - **Name**: *MegaBLAST*
  - **Description**: **

  - **Key**: *s0250*
  - **Name**: *Lowest Commumn Ancestor*
  - **Description**: **

  - **Key**: *s0260*
  - **Name**: *Contig Assembly (Trinity)*
  - **Description**: *Inicio da análise funcional*

  - **Key**: *s0270*
  - **Name**: *Identificação CDS*
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *s0280*
  - **Name**: *Selecionando candidatos para treino/Buscando evidências de candidatos*
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7c1*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7c2*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7c2_2*
  - **Name**: **
  - **Description**: *sed -e "s/lcl|//g"*

  - **Key**: *passo7d1*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7d2*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7e1*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7e2*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7e3*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7f*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7g1*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo7g2*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo8b*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo8c*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo9a*
  - **Name**: **
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo9b*
  - **Name**: **
  - **Description**: *cut -f1,3*

  - **Key**: *passo10*
  - **Name**: *Groupko*
  - **Description**: *Linkar LCA e análise funcional*

  - **Key**: *passo11*
  - **Name**: **
  - **Description**: **

