#21 tocar um mp3

import pygame

pygame.init()
pygame.mixer.music.load('melancholylull.mp3')
pygame.mixer.music.play()
print()
print('digite Enter para parar')
print()
enter = input('')



