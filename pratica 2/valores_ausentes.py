def eh_numero(valor):
    try:
        float(valor)
        return True

    except Exception:
        pass
        
    return False

def calcula_media(arquivo,coluna,separador, possui_cabecalho):
    soma_valores = 0
    qtd_valores  = 0

    f = open(arquivo, "r")
    if(possui_cabecalho): 
        f.readline() # lê a linha do cabeçalho
    
    for linha in f:
        linha = linha.strip("\n")   # remove caractere de quebra de linha
        atributos = linha.split(separador)   # separa os atributos em uma lista

        valor = atributos[coluna-1]
        if eh_numero(valor):   # valor nao ausente
            soma_valores += float(valor)
            qtd_valores  += 1 
    
    f.close()

    media = soma_valores/qtd_valores
    return media

def preenche_ausentes(arquivo,coluna,separador,valor_estimado,possui_cabecalho):
    in_file  = open(arquivo, "r")
    out_file = open("resultado_" + arquivo, "w")   # arquivo de saida com os valores ausentes estimados

    if(possui_cabecalho): # copia o cabeçalho, se existir
        out_file.write(in_file.readline())

    for linha in in_file:
        linha = linha.strip("\n")
        atributos = linha.split(separador)

        valor = atributos[coluna-1]
        if not eh_numero(valor):   # valor ausente
            atributos[coluna-1] = str(valor_estimado)   # substitui valor ausente pelo valor estimado
            linha = separador.join(atributos)   # transforma a lista em uma string
        
        out_file.write(linha + '\n')
    
    in_file.close()
    print(f"Concluído! Arquivo gerado: {out_file.name}")
    out_file.close()

def main():
    arquivo = input("Digite o nome do arquivo: ")
    coluna = int(input("Digite a coluna a ser alterada [1,INF]: "))
    separador = input("Qual o separador usado? ")
    possui_cabecalho_char = input("O arquivo possui cabeçalho? [S/N] ").capitalize()[0]

    if(possui_cabecalho_char != 'S' and possui_cabecalho_char != 'N'):
        raise RuntimeError("Responda 'S' ou 'N' para \"O arquivo possui cabeçalho? [S/N]\".")
    possui_cabecalho = True if possui_cabecalho_char=='S' else False

    '''
    # variaveis de entrada
    arquivo = "teste.csv"   # arquivo de entrada
    coluna = 2   # indice da coluna com valores ausentes
    
    separador = ","   # caractere que separa os atributos
    '''

    media = calcula_media(arquivo,coluna,separador, possui_cabecalho)
    preenche_ausentes(arquivo,coluna,separador,media, possui_cabecalho)

main()