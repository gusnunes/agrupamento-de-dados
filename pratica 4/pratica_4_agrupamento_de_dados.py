# -*- coding: utf-8 -*-

# importando os modulos
import argparse
import pandas as pd
import numpy as np

def write_file(out_df, nome_arquivo_saida):
  out_df.to_csv(nome_arquivo_saida, header=False,index=False)

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
    out_df.loc[x,x] = 0   # diagonal principal zerada

    for y in range(x+1, tamanho):   # acima da diagonal principal
      # objetos do DataFrame
      Ox = in_df.loc[[x]]
      Oy = in_df.loc[[y]]

      distancia = distancia_euclidiana(Ox,Oy)
      out_df.loc[x,y] = distancia
      out_df.loc[y,x] = distancia   # matriz é espelhada
  

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", dest='arquivo', help="Arquivo de entrada", required=True)
  parser.add_argument("-s", "--separador", dest='separador', help="Separador de colunas", default=',')
  parser.add_argument("-c", "--cabecalho", dest='cabecalho', help="Indica se o arquivo possui cabeçalho [True, False]", default='True', choices=['True', 'False'])
  parser.add_argument("-o", "--output", dest='nome_arquivo_saida', help="Arquivo de saída", default='resultado.csv')
  args = parser.parse_args()
  
  arquivo = args.arquivo
  possui_cabecalho = 0 if (args.cabecalho == 'True') else None
  
  # DataFrame de entrada com os objetos
  in_df = pd.read_csv(arquivo, header=possui_cabecalho)
  qtd_linhas, qtd_colunas = in_df.shape

  # DataFrame de saida (conterá a matriz de distancias)
  out_df = pd.DataFrame(index=np.arange(qtd_linhas), columns=np.arange(qtd_linhas))

  # remove as colunas não numéricas
  in_df = in_df.select_dtypes(['number'])   
  
  # reorganiza os indices das colunas (serão números inteiros)
  in_df.columns = [int(indice) for indice in range(0,qtd_colunas)]

  calcula_matriz_distancia(in_df, out_df, qtd_linhas)
  write_file(out_df, args.nome_arquivo_saida)

main()
