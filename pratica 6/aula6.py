import argparse
import random
import pandas as pd
import numpy as np

def write_file(out_df, nome_arquivo_saida):
  out_df.to_csv(nome_arquivo_saida, header=False,index=False)
  print("O resultado foi gravado no arquivo", nome_arquivo_saida)

def calcula_cluster(data=None, kvalue=2 ,n_iteracoes=100, parada_convergencia=0):
  total_elementos = data.shape[0]
  # selecionar k elementos aleatórios
  linhas_selecionadas = []
  while(len(linhas_selecionadas)<kvalue):
    linhas_selecionadas.append(random.randrange(0, total_elementos))
    linhas_selecionadas = list(set(linhas_selecionadas))
  centroides = [data.loc[idx] for idx in linhas_selecionadas]
  data['cluster'] = [-1 for _ in range(total_elementos)]
  # inicializar os critérios de parada
  limite_convergencia = int(total_elementos*parada_convergencia)
  iteracao_corrente = 0

  while True:
    numero_objetos_alterados = 0
    # calcula a distância de cada elemento em relação aos k centroides 
    # e classifica de acordo com o mais próximo
    for idx,elemento in data.iterrows():
      distancias = [distancia_euclidiana(elemento[:-1], centroide) for centroide in centroides]
      centroide_mais_proximo = distancias.index(min(distancias))
      if (elemento['cluster'] != centroide_mais_proximo):
        numero_objetos_alterados += 1
        data.loc[idx, 'cluster'] = centroide_mais_proximo
    
    #se alcançar os criterios de parada, encerra sem calcular o novo centroide
    if(numero_objetos_alterados <= limite_convergencia or iteracao_corrente >= n_iteracoes):
      break

    print(f'\nIteração {iteracao_corrente}')
    # calcula o novo centroide pela média dos elementos do cluster
    for idx, _ in enumerate(centroides):
      aux = data.loc[data['cluster']==idx].drop('cluster', axis=1)
      print(f"Cluster {idx} - {aux.shape[0]} elementos")
      centroides[idx] = aux.mean()
    
    iteracao_corrente += 1
  return data['cluster']

def distancia_euclidiana(x,y):
  # o indice da linha dos dois objetos será 0
  x = x.reset_index(drop=True)
  y = y.reset_index(drop=True)

  n = x.shape[0]   # n atributos (colunas)
  somatorio = 0

  for k in range(n):
    # k-esimo atributo dos objetos
    xk = x.loc[k]
    yk = y.loc[k]
    
    diferenca = xk - yk
    somatorio += diferenca**2

  return somatorio**0.5
  
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", dest='arquivo', help="Arquivo de entrada", required=True)
  parser.add_argument("-k", "--kclusters", dest='kvalue', help="Número de clusters", required=True, type=int)
  parser.add_argument("-s", "--separador", dest='separador', help="Separador de colunas", default=',')
  parser.add_argument("-c", "--cabecalho", dest='cabecalho', help="Indica se o arquivo possui cabeçalho [True, False]", default='True', choices=['True', 'False'])
  parser.add_argument("-o", "--output", dest='nome_arquivo_saida', help="Arquivo de saída", default='resultado.csv')
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

  # seleciona k linhas aleatórias
  if(qtd_linhas < args.kvalue):
    raise ValueError('O número de clusters não pode ser menor que o de objetos')
  separacao_cluster = calcula_cluster(data=in_df, kvalue=args.kvalue)
  
  write_file(separacao_cluster, args.nome_arquivo_saida)

main()