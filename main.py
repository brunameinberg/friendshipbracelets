import pandas as pd
import time

def abrindo_dataframe(name_df):
    df = pd.read_csv(name_df)
    return df

def pode_escrever(palavra, dicionario):
    # Transformar a palavra em maiúsculas e remover espaços para a comparação
    palavra_comparacao = palavra.upper().replace(" ", "")
    
    # Criar uma cópia do dicionário para não alterar o original
    dic_temp = dicionario.copy()
    
    # Iterar por cada letra da palavra
    for letra in palavra_comparacao:
        # Se a letra não estiver no dicionário ou sua quantidade for 0, retorna False
        if letra not in dic_temp or dic_temp[letra] == 0:
            return False
        
        # Decrementar a quantidade da letra no dicionário temporário
        dic_temp[letra] -= 1
        
    # Se todas as letras da palavra foram encontradas no dicionário, retorna True
    return True


def main(df, infos):
    # Filtrar o DataFrame baseado nas palavras que podem ser escritas
    df_filtrado = df[df['Bracelet Text'].apply(lambda x: pode_escrever(x, infos))]
    
    # Retornar apenas as palavras formadas possíveis
    return df_filtrado['Bracelet Text'].tolist()



if __name__ == "__main__":
    name_df = "dados/ideias.csv"
    df = abrindo_dataframe(name_df)

    print("Para gerarmos as possíveis opções de pulseira precisamos das seguintes informações: \n")
    time.sleep(1)
    print("O formato de recebimento obedece o seguinte: \n")
    time.sleep(1)
    print("Letra: A \n")
    time.sleep(1)
    print("Quantidade: 3 \n")
    time.sleep(1)
    print("Caso não deseje mais adicionar pulseiras digite: - \n")
    time.sleep(1)
    print("Vamos começar!!!\n") 
    time.sleep(1)
    infos = {}
    while infos.keys() != "-":
        letra = input("Digite a letra: ")
        if letra == "-":
            break
        quantidade = int(input("Digite a quantidade: "))
        infos[letra] = quantidade
    '''    infos = {
    'E': 5,
    'R': 4,
    'A': 4,
    'S': 3,
    'T': 4,
    'O': 3,
    'U': 3,
    'I': 3,
    'M': 2,
    'N': 2,
    'C': 2,
    'L': 1,
    'B': 2
    }'''
    
    print(infos)
    print(main(df, infos))