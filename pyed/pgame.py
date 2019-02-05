from sys import exit
import pygame
from pygame.locals import *
import time
import random

pygame.init()

#screen width x height
SCREEN_SIZE = (800, 480)

#Initializing screen with no caption
pgDisplay = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
pgDisplay1 = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
pgDisplay2 = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
clock = pygame.time.Clock()
buttons = []

#Variables
myfont = pygame.font.SysFont('Comic Sans MS', 50)
title = myfont.render('Photo Booth!', True, (0, 0, 0))
startcam = myfont.render('Press to Start!', True, (0, 0, 0))
pose = myfont.render('STRIKE A POSE!', True, (0, 0, 0))
img3 = myfont.render('3', True, (0, 0, 0))
img2 = myfont.render('2', True, (0, 0, 0))
img1 = myfont.render('1', True, (0, 0, 0))

#Colors
green = (0, 125, 0)

def photo_loop():

    ploop = True

    while ploop:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pgDisplay2.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(1)

        pgDisplay2.fill((255, 255, 255))
        pgDisplay2.blit(pose, (200, 250))
        pygame.display.flip()
        time.sleep(1)

        pgDisplay2.fill((255, 255, 255))
        pgDisplay2.blit(img3, (200, 250))
        pygame.display.flip()
        time.sleep(1)

        pgDisplay2.fill((255, 255, 255))
        pgDisplay2.blit(img2, (200, 250))
        pygame.display.flip()
        time.sleep(1)

        pgDisplay2.fill((255, 255, 255))
        pgDisplay2.blit(img1, (200, 250))
        pygame.display.flip()
        time.sleep(1)
        pygame.display.flip()

        ploop = False

        pygame.display.flip()
        clock.tick(15)
    main_loop()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Fills the screen and displays the title image
        pgDisplay.fill((255, 255, 255))
        pgDisplay.blit(title, (350, 10))

        #Drawing the Green area for the button
        pygame.draw.rect(pgDisplay, green, (150, 350, 100, 50))

        mouse = pygame.mouse.get_pos()

        # Ends the Intro Loop when the mouse is clicked on the green button

        if event.type == MOUSEBUTTONDOWN and 150+100 > mouse[0] > 150 and 350+50 > mouse[1] > 350:
            #pygame.draw.rect(pgDisplay, green, (150, 450, 100, 50))
            #print('Hello')
            #pgDisplay1.fill((125, 125, 125))
            intro = False

        pygame.display.flip()
        clock.tick(15)

#Main loop
def main_loop():

    mloop = True

    while mloop:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pgDisplay1.fill((255, 255, 255))
        pgDisplay1.blit(title, (350, 10))
        pgDisplay1.blit(startcam, (200, 250))

        #pygame.draw.rect(pgDisplay1,(255, 255, 255),(300, 250, 250, 150))

        mouse = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN and 300+250 > mouse[0] > 300 and 250+150 > mouse[1] > 250:
            print("let's Go!")
            mloop = False
            photo_loop()

        pygame.display.flip()
        clock.tick(15)

game_intro()
main_loop()
