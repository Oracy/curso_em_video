import pygame

pygame.init()
pygame.mixer.music.load('./files/Diga_Parte_Dois.mp3')
pygame.mixer.music.play()
pygame.event.wait()