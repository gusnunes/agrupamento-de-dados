Disciplina: Agrupamento de Dados
Professora: Elaine Ribeiro
Alunos: Danilo Augusto\11611BCC021
	João M. Gomes \11611BCC043


1 - COMO EXECUTAR:

No arquivo "valores_ausentes.py" está implementada a técnica sobre valores ausentes vista em aula.

Para executar o código, é necessário abrir o prompt de comando (cmd, powershell ou terminal) e informar os valores de nome do arquivo e o 
índice da coluna a ser alterada. Como resultado da execução do código, será gerado um outro .csv, iniciando com "resultado_" concatenado 
com o nome do arquivo.
Se necessário, podem ser alteradas as flags do separador de colunas e do cabeçalho presente:

1.1 - FLAGS:
 __________________________________________________________________________________
|Flag		| Valores					 	| Default  |
|----------------------------------------------------------------------------------|
|-c/--cabecalho	|True se o arquivo possuir cabeçalho, senão False	| True	   |	
|-s/--separador	|Qualquer valor a ser usado como separador de colunas	| ,	   |
|__________________________________________________________________________________|

2 - EXEMPLO DE EXECUÇÃO:

O arquivo 'TEJ - Normalized_2013_0430_Taiwan_data_modificado.csv' foi alterado para adição de valores ausentes nas colunas de índices 2, 3, 
7 e 9. Como o arquivo possui cabeçalho e o caractere ',' como separador, não é necessário o uso de flags. Para o preenchimento da coluna 2, 
após abrir o prompt de comando, é necessário informar os seguintes valores:

----------------------------------------------------------------------------------------------------------
Preenchimento dos valores da coluna de índice 2 em 'TEJ - Normalized_2013_0430_Taiwan_data_modificado.csv'
----------------------------------------------------------------------------------------------------------
>> python valores_ausentes.py
Digite o nome do arquivo:
>> TEJ - Normalized_2013_0430_Taiwan_data_modificado.csv
Digite a coluna a ser alterada [1,INF]:
>> 2
Concluído! Arquivo gerado: resultado_TEJ - Normalized_2013_0430_Taiwan_data_modificado.csv
----------------------------------------------------------------------------------------------------------
Obs.: '>>' Indica os campos com interação do usuário.