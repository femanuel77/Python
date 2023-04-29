import pygame
pygame.init()
pygame.mixer.music.load('rapasta.mp3')
pygame.mixer.music.play(loops=-1)
pygame.event.wait()