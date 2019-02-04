from sys import exit
import pygame
from pygame.locals import *
#import time
import random

pygame.init()

#screen width x height
SCREEN_SIZE = (800, 600)

#Initializing screen with no caption
pgDisplay = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
pgDisplay1 = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
#clock = pygame.time.Clock()
buttons = []

myfont = pygame.font.SysFont('Comic Sans MS', 50)
title = myfont.render('P-Pie!', True, (0, 0, 0))

#Colors
green = (0, 125, 0)

class Window():
    def __init__(self, screen, position, size):
        self.screen = screen
        self.rect = Rect(position, size)


class Button():
    def __init__(self, parent, position, size, color):
        self.parent = parent
        self.position = position
        self.size = size
        self.color = color

    def get_event(selfs, event):
        pgDisplay.fill(125, 125, 125)
        pygame.display.flip()

    def create_button(self):
        newwindow = Window(pgDisplay1, (10, 10), SCREEN_SIZE)
        newbutton = Button(newwindow, (150, 250), (100, 50), pygame.Color('Pink'))
        buttons.append(newbutton)
        newbutton.draw()



def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pgDisplay.fill((255, 255, 255))
        pgDisplay.blit(title, (350, 10))

        pygame.draw.rect(pgDisplay, green, (150, 450, 100, 50))

        mouse = pygame.mouse.get_pos()

        if  event.type == MOUSEBUTTONUP and 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(pgDisplay, green, (150, 450, 100, 50))
            print('Hello')
            pgDisplay1.fill((125, 125, 125))

        pygame.display.update()
        #clock.tick(15)



game_intro()
