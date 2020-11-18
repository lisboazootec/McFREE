# McFREE

MCFREE is a rapid, automated, and efficient metatranscriptome pipeline for analyzing large RNA-seq datasets in Docker containers for supercomputing cluster environments. MCFREE was born out of a need for metatranscriptome without repetition, annotated, and free of chimeras using the Megablast algorithm for taxonomic annotation.

![Workflow](McFREE.tif)

## Formato do arquivo [variables.py](variables.py)
Este arquivo deve seguir primeiramente a [sintaxe](https://docs.python.org/3.6/reference/index.html) da linguagem [Python3.6](https://www.python.org/). Além disso, este arquivo contém variáveis que são utilizadas em diferentes partes da aplicação (_files_, _steps_ ,_runners_):

* **files**: Um dicionário onde os valores são os caminhos para arquivos e pastas referenciadas nos argumentos da pipeline. As _keys_ são os nomes (variáveis) das referências para estes aquivos, utilizadas nos comandos, p.ex.:
	
	```python
	{
		"home": "/home/user",
		"sequences": "{home}/sequences",
		"file_to_cut": "{sequences}/registros.tsv",
		"file_from_cut": "{sequences}/registros.cutted.tsv",
	}
	```
	
* **steps**: Uma lista de dicionários com atributos predeterminados. Os valores devem estar de acordo com a descrição e exemplos abaixo:
	
	* _index_: Um código único e que indique o índice do _step_ na sequência (ordenação de string);
	* _runner_: O nome do comando que será o executor do _step_. Poderá ser o nome de uma rotina segundo o sistema operacional (OS), de forma literal. Caso não seja uma rotina conhecida pelo OS, deve ser especificado a forma de execução na variável __runners__, neste caso, o nome é uma referência.
	* _args_: Argumentos que serão acrescentados ao _runner_ para a execução. Caso o _runner_ seja uma referência para uma função estes argumentos devem conter sempre uma _key_ precedida de `--`.
	* _name_: Um nome curto para o _step_.
	* _description_: Uma descrição suscinta da ação do step;

	Exemplo:

	```python
	[
		{
			"index": "s0100",
			"runner": "cut",
			"args": "-f1,2 {file_to_cut} > {file_from_cut}",
			"name": "Filtra colunas",
			"description": "Filtra somente colunas 1 e 2 do arquivo tabular de registros."
		},{
			"index": "s0200",
			"runner": "remove_dup",
			"args": "--file {file_from_cut} --unique-col 1",
			"name": "Agrupa linhas",
			"description": "Matém somente as linhas únicas no arquivo, tomando com base a coluna 1. Também conta as repetições de cada linha."
		}
	]
	```

* **runners**: Um dicionário com os comandos não-nativos do OS. O valor pode ser tanto uma string como uma função. Uma string quando trata-se de um inicializador a partir de outro arquivo. Uma função quando trata-se de uma rotina escrita em python, neste caso a função deve estar definina/importada no arquivo [utils.py](utils.py). Também no caso de função, em __steps__ devem ser especificadas as _keys_ para todos os argumentos da chamada, até mesmo os arqgumentos posicionais.

	Exemplo:

	```python
	{
		"remove_dup":remove_dup_function,
		"another_prog": "perl another-program.perl",
	}
	```




