Disciplina: Agrupamento de Dados
Professora: Elaine Ribeiro
Alunos: 
    Danilo Augusto\11611BCC021
	João M. Gomes \11611BCC043


1 - COMO EXECUTAR:

No arquivo "matriz_distancia.py" está implementada a técnica sobre vista em aula. O código faz uso 
das bibliotecas numpy e pandas, e por isso, a instalação das bibliotecas pode ser necessária. Para 
executar o código, é necessário abrir o prompt de comando (cmd, powershell ou terminal) e executar 
o arquivo matriz_distancia.py, informando por meio da flag, o nome do arquivo com a base de dados 
a ser usada. Como resultado da execução do código, será gerado um arquivo csv. Caso o nome do arquivo 
de saída não seja informado com a flag -o/--output, o resultado será gravado no arquivo 'resultado.csv'.
Se necessário, podem ser alteradas as flags do separador de colunas e do cabeçalho, de acordo com 
a base de dados usada.

1.1 - ARQUIVOS:

- O arquivo 'processed.cleveland.csv' possui os dados processados da base Heart Disease Data Set 
(https://archive.ics.uci.edu/ml/datasets/heart+disease), e foi alterado apenas para remoção de 
valores ausentes.

- O arquivo 'matriz_distancia.py' gera a matriz de distância de uma base de dados e a registra em
um arquivo no seguinte formato:

  Dist(O1,O1), Dist(O1,O2), Dist(O1,O3),.... Dist(O1,ON)
  Dist(O1,O1), Dist(O1,O2), Dist(O1,O3),.... Dist(O1,ON)
  Dist(O2,O1), Dist(O2,O2), Dist(O2,O3),.... Dist(O2,ON)
  ...
  Dist(ON,O1), Dist(ON,O2), Dist(ON,O3),.... Dist(ON,ON)

Onde Dist(OX,OY) indica o valor da distância entre os objetos (instâncias).

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
|-o/--output	| Nome do arquivo de saída								|'resultado.csv'|
|-c/--cabecalho	| True se o arquivo possuir cabeçalho, senão False	    | True			|	
|-s/--separador	| Qualquer valor a ser usado como separador de colunas	|   ,	  		|
 ---------------------------------------------------------------------------------------

2 - EXEMPLO DE EXECUÇÃO:

- Abaixo é exemplificado o uso do código para a geração da matriz da base processed.cleveland, 
e do arquivo 'resultado_cleveland':

---------------------------------------------------------------------------------------------
>> python matriz_distancia.py -i 'processed.cleveland.csv' -o 'resultado_cleveland.csv'
---------------------------------------------------------------------------------------------
Obs.: '>>' Indica os campos com interação do usuário.