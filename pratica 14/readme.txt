Disciplina: Agrupamento de Dados
Professora: Elaine Ribeiro
Alunos: 
    Danilo Augusto\11611BCC021
	João M. Gomes \11611BCC043


1 - COMO EXECUTAR:


No arquivo "silhueta.py" está implementada a técnica do algoritmo single link, e para a sua execução são 
necessários os arquivos 'resultado_single_link.csv' e 'resultado_k_means.csv'. Ao final da execução do 
algoritmo, aparecerá na tela o resultado para ambos os testes e qual dos testes se saiu melhor.

No arquivo "kmeans.py" está implementada a técnica do k-means vista em aula. O código faz uso 
das bibliotecas numpy e pandas, e por isso, a instalação das bibliotecas pode ser necessária. Para 
executar o código, é necessário abrir o prompt de comando (cmd, powershell ou terminal) e executar 
o arquivo k-means.py, informando por meio da flag, o nome do arquivo com a base de dados a ser usada 
e o número de clusters desejado. Como resultado da execução do código, será gerado um arquivo csv.
Caso o nome do arquivo de saída não seja informado com a flag -o/--output, o resultado será gravado 
no arquivo 'resultado_k_means.csv'. Se necessário, podem ser alteradas as flags do separador de colunas e 
do cabeçalho, de acordo com a base de dados usada.

No arquivo "single_link.py" está implementada a técnica do algoritmo single link, e sua execução segue
os protocolos mencionados acima, sendo que o resultado é adicionado ao arquivo 'resultado_single_link.csv'

1.1 - BASE DE DADOS:

- O arquivo 'iris.csv' possui os dados processados da base Iris Data Set
(https://archive.ics.uci.edu/ml/datasets/iris), que possui 3 classes com 50 elementos cada. Uma das 
classes é separável linearmente, porém as outras duas não são. O arquivo 'iris_no_label.csv' possui a 
mesma base de dados, sem os rótulos para classificação

1.2 - BIBLIOTECAS:

- A bilioteca numpy pode ser instalada usando os comandos:
>> pip install numpy
ou 
>> conda install numpy

- A bilioteca pandas pode ser instalada usando os comandos:
>> pip install pandas
ou 
>> conda install pandas

1.3 - FLAGS:
 ____________________________________________________________________________________________
|Flag			| Valores					| Default  	     |
|--------------------------------------------------------------------------------------------|
|-i/--input	| Nome do arquivo de entrada (obrigatório)	        | 		     |
|-k/--kclusters	| Número de clusters desejado (obrigatório)             | 		     |	
|-o/--output	| Nome do arquivo de saída				|<depende do arquivo>|
|-c/--cabecalho	| True se o arquivo possuir cabeçalho, senão False      | True		     |	
|-s/--separador	| Qualquer valor a ser usado como separador de colunas	|   ,	  	     |
 --------------------------------------------------------------------------------------------

2 - EXEMPLO DE EXECUÇÃO:


- Para rodar o algoritmo silhueta, o código abaixo deve ser usado no prompt de comando. Como os arquivos
'resultado_single_link.csv' e 'resultado_k_means.csv' são necessários para a execução do algoritmo, abaixo
também estão indicadas as formas de geração dos dois arquivos:
---------------------------------------------------------------------------------------------
>> python silhueta.py
---------------------------------------------------------------------------------------------


- Abaixo é exemplificado o uso do código para a geração dos grupos da base iris
no arquivo 'resultado_k_means.csv':
---------------------------------------------------------------------------------------------
>>  python kmeans.py -i iris_no_label.csv -s ',' -c False -k 3
---------------------------------------------------------------------------------------------

- Abaixo é exemplificado o uso do código para a geração dos grupos da base iris
no arquivo 'resultado_single_link.csv':
---------------------------------------------------------------------------------------------
>> python single_link.py -i iris_no_label.csv -s ',' -c False -k 3
---------------------------------------------------------------------------------------------