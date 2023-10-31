import pygame
import os
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('/home/alarm/project/src/shark.wav')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
