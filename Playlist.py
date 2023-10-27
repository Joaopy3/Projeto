#Filtra os arquivos que são mp3 na pasta

import os

def pegarArquivos_mp3_Filtrados(pasta,tipo):
    arquivos_diretorios = os.listdir(pasta)
    arquivos = ([arquivos for arquivos in arquivos_diretorios if arquivos.endswith(tipo)])
    return "\n".join(arquivos)
print(pegarArquivos_mp3_Filtrados('D:\Tabata II','mp3'))