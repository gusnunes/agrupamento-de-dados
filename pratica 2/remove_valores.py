import random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def remove_valores(arquivo, coluna, num_linhas, separador, char_vazio):
    f = open(arquivo, "r")
    tamanho_arquivo = file_len(arquivo)

    if(tamanho_arquivo <= num_linhas):
        raise RuntimeError(f"O arquivo possui menos de {num_linhas} linhas.")
    
    linhas_apagadas = set()

    while(len(linhas_apagadas) < num_linhas):
        linhas_apagadas.add(random.randint(1, tamanho_arquivo))
    linhas_apagadas = sorted(linhas_apagadas)
    linha_atual = 1
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

    if(remove_valores(arquivo, coluna, num_linhas, separador, char_vazio)):
        print(f"O resultado da modificação está em {arquivo.split('.')[0]}_modificado.{arquivo.split('.')[1]}")



