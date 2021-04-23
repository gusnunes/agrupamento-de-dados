Disciplina: Agrupamento de Dados
Professora: Elaine Ribeiro
Alunos: 
    Danilo Augusto\11611BCC021
	João M. Gomes \11611BCC043


1 - COMO EXECUTAR:

No arquivo "k-means.py" está implementada a técnica sobre vista em aula. O código faz uso 
das bibliotecas numpy e pandas, e por isso, a instalação das bibliotecas pode ser necessária. Para 
executar o código, é necessário abrir o prompt de comando (cmd, powershell ou terminal) e executar 
o arquivo k-means.py, informando por meio da flag, o nome do arquivo com a base de dados a ser usada 
e o número de clusters desejado. Como resultado da execução do código, será gerado um arquivo csv.
Caso o nome do arquivo de saída não seja informado com a flag -o/--output, o resultado será gravado 
no arquivo 'resultado.csv'. Se necessário, podem ser alteradas as flags do separador de colunas e 
do cabeçalho, de acordo com a base de dados usada.

1.1 - ARQUIVOS:

- O arquivo 'iris.data' possui os dados processados da base Iris Data Set
(https://archive.ics.uci.edu/ml/datasets/iris), que possui 3 classes com 50 elementos cada. Uma das 
classes é separável linearmente, porém as outras duas não são.

- O arquivo 'k-means.py' gera um arquivo que indica para qual cluster cada elemento da base de
dados foi mapeado.

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
 _______________________________________________________________________________________
|Flag			| Valores											 	| Default  	    |
|---------------------------------------------------------------------------------------|
|-i/--input		| Nome do arquivo de entrada (obrigatório)			    | 			    |
|-k/--kclusters	| Número de clusters desejado (obrigatório)			    | 			    |	
|-o/--output	| Nome do arquivo de saída								|'resultado.csv'|
|-c/--cabecalho	| True se o arquivo possuir cabeçalho, senão False	    | True			|	
|-s/--separador	| Qualquer valor a ser usado como separador de colunas	|   ,	  		|
 ---------------------------------------------------------------------------------------

2 - EXEMPLO DE EXECUÇÃO:

- Abaixo é exemplificado o uso do código para a geração dos grupos da base iris
no arquivo 'resultado_iris':
---------------------------------------------------------------------------------------------
>> python k-means.py -i iris.data -k 3 -o resultado_iris.csv -c False
Iteração 0
Cluster 0 - 51 elementos
Cluster 1 - 46 elementos
Cluster 2 - 53 elementos
...
Iteração 3
Cluster 0 - 50 elementos
Cluster 1 - 39 elementos
Cluster 2 - 61 elementos
O resultado foi gravado no arquivo resultado_iris.csv
---------------------------------------------------------------------------------------------
Obs1.: '>>' Indica os campos com interação do usuário.
Obs2.: O número de iterações e de elementos por cluster a cada iteração podem mudar de acordo com
	   elementos selecionados randomicamente como clusters na primeira iteração.