
arquivos = []

import os

import pygame

def pegarArquivos_Filtrados(pasta,tipo):

    global arquivos

    arquivos_diretorios = os.listdir(pasta)
    arquivos = ([arquivos for arquivos in arquivos_diretorios if arquivos.endswith(tipo)])
    return "\n".join(arquivos)

def tocarMusicas(indice,pasta):

    import keyboard

    def inicializarPlaylist():

        nonlocal indice

        busy = True
        pausa = False
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(pasta,arquivos[indice]))
        pygame.mixer.music.set_volume(0.6)
        pygame.time.delay(1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() or busy:
            pygame.time.Clock().tick(10)
            if keyboard.is_pressed('f2'):
                pygame.mixer.music.pause()
                busy = True
                pausa = True
            if keyboard.is_pressed('f4'):
                pygame.mixer.music.unpause()
                busy = True
                pausa = False
            if keyboard.is_pressed('f7'):
                pygame.mixer.music.stop()
                busy = False
            if keyboard.is_pressed('f8'):
                pygame.mixer.music.stop()
                busy = False
                indice -= 2
            if not pygame.mixer.music.get_busy() and not pausa:
                break

    def continuarPlaylist():
        try:
            while True:
                inicializarPlaylist()
                nonlocal indice
                indice += 1
        except IndexError:
            pygame.quit()

    continuarPlaylist()




