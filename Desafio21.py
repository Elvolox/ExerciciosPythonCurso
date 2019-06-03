import pygame
pygame.init()#iniciando o pygame
pygame.mixer.music.load('ex01.mp3')#Importando a musica
pygame.mixer.music.play()#tocar a musica
pygame.event.wait()#pausar a musica