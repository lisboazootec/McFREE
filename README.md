# McFREE

MCFREE is a rapid, automated, and efficient metatranscriptome pipeline for analyzing large RNA-seq datasets in Docker containers for supercomputing cluster environments. MCFREE was born out of a need for metatranscriptome without repetition, annotated, and free of chimeras using the Megablast algorithm for taxonomic annotation.

![Workflow](McFREE.png)

# Requirements 

* **[Docker](https://www.docker.com/)**.
* **[Python -- v3.0 or newer](https://www.python.org/)**.
* **[R version -- v4.0.3 or newer](https://cran.r-project.org/)**.

# Dependencies 

* **[FastqJoin](https://github.com/ExpressionAnalysis/ea-utils/blob/wiki/FastqJoin.md)**.
* **[HS-BLASTn](https://github.com/chenying2016/queries/tree/master/hs-blastn-src)**.
* **[Trinity](https://github.com/trinityrnaseq/trinityrnaseq)**.
* **[TransDecoder](https://github.com/TransDecoder/TransDecoder/wiki)**.
* **[AC-DIAMOND](https://github.com/Maihj/AC-DIAMOND)**.
* **[CORNAS R package](https://github.com/joel-lzb/CORNAS)**.
