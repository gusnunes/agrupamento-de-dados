import argparse
from numpy import append
import pandas as pd
import random

def distancia_euclidiana(x,y):
  n = x.shape[0]   # n atributos (colunas)
  somatorio = 0

  for k in range(n):
    # k-esimo atributo dos objetos
    xk = x.iloc[k]
    yk = y.iloc[k]
    
    diferenca = float(xk) - float(yk)
    somatorio += diferenca**2

  return somatorio**0.5

def largura_silhueta(data,qtd_grupos):
  # largura da silhueta simplificada
  SSWC = 0

  # calcula os centroides dos grupos
  centroides = [None]*qtd_grupos
  for idx, _ in enumerate(centroides):
    aux = data.loc[data['cluster']==idx].drop('cluster', axis=1)
    centroides[idx] = aux.mean(axis=0)
  #print(centroides[0])
  for _,elemento in data.iterrows():
    # dissimilaridade média do objeto ao seu cluster
    elemento_cluster = int(elemento["cluster"])
    #print(elemento[:-1])
    elemento_centroide = distancia_euclidiana(elemento[:-1], centroides[elemento_cluster])

    # distância do objeto aos clusters vizinhos
    distancias = []
    for idx,centroide in enumerate(centroides):
      if idx != elemento_cluster:
        distancias.append(distancia_euclidiana(elemento[:-1], centroide))
    
    # dissimilaridade média do objeto ao seu cluster vizinho mais próximo
    centroide_mais_proximo = min(distancias)

    diferenca = centroide_mais_proximo - elemento_centroide
    maior_distancia = max(centroide_mais_proximo,elemento_centroide) + 0.0000000001
    silhueta_elemento = diferenca/maior_distancia
    SSWC += silhueta_elemento
  
  # quantidade de elementos da base
  N = data.shape[0]
  
  return SSWC/N
   
def main():

  # DataFrame de entrada com os objetos
  in_df = pd.read_csv('resultado_single_link.csv', header=0)
  resultado1 = largura_silhueta(in_df,len(in_df['cluster'].unique()))
  in_df = pd.read_csv('resultado_k_means.csv', header=0)
  resultado2 = largura_silhueta(in_df,len(in_df['cluster'].unique()))
  print(f"Resultado Single Link = {resultado1}")
  print(f"Resultado K-Means = {resultado2}")
  if(resultado2 == resultado1):
    print("Os dois algoritmos obtiberam o mesmo resultado!")
  elif(resultado1 > resultado2):
    print("O resultado do algoritmo Single Link foi melhor!")
  else:
    print("O resultado do algoritmo K-Means foi melhor!")
    

main()