from sys import exit
import pygame
from pygame.locals import *
import time
import random

pygame.init()

#screen width x height
SCREEN_SIZE = (800, 600)

#Initializing screen with no caption
pgDisplay = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)

clock = pygame.time.Clock()
button = []

myfont = pygame.font.SysFont('Comic Sans MS', 30)
title = myfont.render('P-Pie!', True, (255,255,255))

class Window():
    def __init__(self, screen, position, size):
        self.screen = screen
        self.rect = Rect(position, size)




def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pgDisplay.fill((0,0,0))


        pgDisplay.blit(title, (350,10))

        pygame.display.update()
        clock.tick(15)


game_intro()