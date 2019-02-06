from sys import exit
import pygame
from pygame.locals import *
import time
import random
#from pgame import *

pygame.init()

#screen width x height
SCREEN_SIZE = (800, 480)

setupDisplay = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
clock = pygame.time.Clock()
buttons = []


myfont = pygame.font.SysFont('Arial', 50)
title = myfont.render('Photo Booth setup!', True, (0, 0, 0))


setupFont = pygame.font.SysFont('Arial', 20)
back = setupFont.render('Back', True, (0, 0, 0))

def setup_loop():

    sloop = True

    while sloop:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        setupDisplay.fill((255, 255, 255))
        setupDisplay.blit(title, (250, 10))
        setupDisplay.blit(back, (710, 440))
        mouse = pygame.mouse.get_pos()



        if event.type == MOUSEBUTTONDOWN and 690+800 > mouse[0] > 690 and 410+480 > mouse[1] > 410:
            print("button pressed")
            sloop = False
            time.sleep(.5)
            #game_intro()

        pygame.display.flip()
        clock.tick(15)

