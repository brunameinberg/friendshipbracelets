from django.shortcuts import render
import pandas as pd
import os

# Construa o caminho para o arquivo CSV
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados', 'ideias.csv')

df = pd.read_csv(csv_path)

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


def index(request):
    if request.method == 'POST':
        infos = {}
        for key in request.POST:
            # Certifique-se de processar apenas as chaves esperadas (letras e números)
            if key.isalpha() or key.isdigit():
                try:
                    infos[key.upper()] = int(request.POST[key])
                except ValueError:
                    pass  # ignora valores que não podem ser convertidos para int
        palavras_possiveis = main(df, infos)
        return render(request, 'resultado.html', {'palavras': palavras_possiveis})
    return render(request, 'entrada_letras_numeros.html')
