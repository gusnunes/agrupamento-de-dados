import random

def n_linhas_arq(arquivo):
    with open(arquivo) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def remove_valores(arquivo, coluna, num_linhas, separador, char_vazio, possui_cabecalho):

    tamanho_cabecalho = 1 if possui_cabecalho else 0
    f = open(arquivo, "r")
    tamanho_arquivo = n_linhas_arq(arquivo)

    if(tamanho_arquivo-tamanho_cabecalho <= num_linhas):
        raise RuntimeError(f"O arquivo possui menos que {num_linhas} linhas de dados.")
    
    linhas_apagadas = set()

    while(len(linhas_apagadas) < num_linhas):
        linhas_apagadas.add(random.randint(tamanho_cabecalho, tamanho_arquivo))
    linhas_apagadas = sorted(linhas_apagadas)
    linha_atual = 0
    index_linhas_apagadas = 0

    with open(arquivo.split('.')[0]+"_modificado."+arquivo.split('.')[1], "w") as f_modificado:
        for linha in f:
            if(index_linhas_apagadas < len(linhas_apagadas) and 
                        linha_atual == linhas_apagadas[index_linhas_apagadas]):
                linha = linha.strip("\n")   # remove caractere de quebra de linha
                atributos = linha.split(separador)   # separa os atributos em uma lista
                atributos[coluna-1] = char_vazio
                f_modificado.write(separador.join(atributos)+"\n")
                index_linhas_apagadas += 1
            else: 
                f_modificado.write(linha)
            linha_atual += 1          
        f.close()
    return True

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo: ")
    coluna = int(input("Digite a coluna a ser alterada [1,INF]: "))
    num_linhas = int(input("Quantas linhas devem ser removidas? "))
    separador = input("Qual o separador usado? ")
    char_vazio = input("Insira a representação a ser usada nos valores vazios: ")
    possui_cabecalho_char = input("O arquivo possui cabeçalho? [S/N] ").capitalize()[0]

    if(possui_cabecalho_char != 'S' and possui_cabecalho_char != 'N'):
        raise RuntimeError("Responda 'S' ou 'N' para \"O arquivo possui cabeçalho? [S/N]\".")
    possui_cabecalho = True if possui_cabecalho_char=='S' else False    

    if(remove_valores(arquivo, coluna, num_linhas, separador, char_vazio, possui_cabecalho)):
        print(f"O resultado da modificação está em {arquivo.split('.')[0]}_modificado.{arquivo.split('.')[1]}")



