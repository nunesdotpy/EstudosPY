# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
from pygame import mixer
mixer.init()
mixer.music.load("music.mp3")
mixer.music.set_volume(1)
mixer.music.play()
a = input("A treta é so com o peidado do hylander")
a = input("HY-HYLANDER COMÉDIA, ROBAMO OS TEU ICE")
