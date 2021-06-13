#main.py
# importando os modulos
import argparse
import pandas as pd
import numpy as np

def print_matrix(mat):
  for i in mat:
    print(i)

def distancia_euclidiana(x,y):
  # o indice da linha dos dois objetos será 0
  x = x.reset_index(drop=True)
  y = y.reset_index(drop=True)

  n = x.shape[1]   # n atributos (colunas)
  somatorio = 0

  for k in range(n):
    # k-esimo atributo dos objetos
    xk = x.loc[0,k]
    yk = y.loc[0,k]
    
    diferenca = xk - yk
    somatorio += diferenca**2

  return somatorio**0.5

def calcula_matriz_distancia(in_df,out_df,tamanho):
  for x in range(tamanho):
    out_df.loc[x,x] = 0   # diagonal principal = infinito

    for y in range(x+1, tamanho):   # acima da diagonal principal
      # objetos do DataFrame
      Ox = in_df.loc[[x]]
      Oy = in_df.loc[[y]]

      distancia = distancia_euclidiana(Ox,Oy)
      out_df.loc[x,y] = distancia
      out_df.loc[y,x] = distancia   # matriz é espelhada

def select_min_reduce(out_df):
    out_df.rename(index=str, columns=str)
    colunas = out_df.columns
    col_menor=0
    row_menor = 0
    menor_elemento = np.inf
    for idx, col in enumerate(colunas):
        aux = out_df[out_df.gt(0)][col].min()
        if(aux < menor_elemento):
            menor_elemento = aux
            col_menor = col
            row_menor = out_df[out_df[col] == aux].index[0]
    row_1, row_2 = out_df.loc[col_menor], out_df.loc[row_menor]
    col_1, col_2 = out_df.loc[:, col_menor], out_df.loc[:, row_menor]

    for idx in range(len(row_1)):
      if (row_1.iloc[idx] > row_2.iloc[idx]):
        row_1.iloc[idx] = row_2.iloc[idx]
        col_1.iloc[idx] = col_2.iloc[idx]
    
    out_df.loc[:, col_menor] = col_1
    out_df.loc[row_menor, :] = row_1
    out_df.rename(columns={col_menor:str(col_menor)+", "+str(row_menor)}, inplace=True)
    out_df.rename(index={col_menor:str(col_menor)+", "+str(row_menor)}, inplace=True)
    out_df = out_df.drop(row_menor, axis=1)
    out_df = out_df.drop(row_menor)
    return out_df
  
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", dest='arquivo', help="Arquivo de entrada", required=True)
  parser.add_argument("-s", "--separador", dest='separador', help="Separador de colunas", default=',')
  parser.add_argument("-c", "--cabecalho", dest='cabecalho', help="Indica se o arquivo possui cabeçalho [True, False]", default='True', choices=['True', 'False'])
  args = parser.parse_args()
  
  arquivo = args.arquivo
  possui_cabecalho = 0 if (args.cabecalho == 'True') else None
  
  # DataFrame de entrada com os objetos
  in_df = pd.read_csv(arquivo, header=possui_cabecalho)
  
  # remove as colunas não numéricas
  in_df = in_df.select_dtypes(['number'])   

  # reorganiza os indices das colunas (serão números inteiros)
  qtd_linhas, qtd_colunas = in_df.shape
  in_df.columns = [int(indice) for indice in range(0,qtd_colunas)]

  # DataFrame de saida (conterá a matriz de distancias)
  out_df = pd.DataFrame(index=np.arange(qtd_linhas), columns=np.arange(qtd_linhas))
  calcula_matriz_distancia(in_df, out_df, qtd_linhas)
  print(out_df)
  while(len(out_df.columns) > 1):
    out_df = select_min_reduce(out_df)
    print("\n\n\n")
    print(out_df)

main()
