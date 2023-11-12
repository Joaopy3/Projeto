
arquivos = []

import os

def pegarArquivos_Filtrados(pasta,tipo):

    global arquivos

    arquivos_diretorios = os.listdir(pasta)
    arquivos = ([arquivos for arquivos in arquivos_diretorios if arquivos.endswith(tipo)])
    return "\n".join(arquivos)

def tocarMusicas(indice,pasta):

    import pygame

    def inicializarPlaylist():

        nonlocal indice

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(pasta,arquivos[indice]))
        pygame.mixer.music.set_volume(0.6)
        pygame.time.delay(1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def continuarPlaylist():
        try:
            while True:
                inicializarPlaylist()
                nonlocal indice
                indice += 1
        except IndexError:
            pygame.quit()

    continuarPlaylist()

tocarMusicas(0,caminho)


