from sys import exit
import pygame
from pygame.locals import *

SCREEN_SIZE = (500, 480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
#screen_center = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1]/2)



#Images pb = pygame.display.set_mode((500, 480))
bg = pygame.image.load('images/background.png')
snap = pygame.image.load('images/snap.png')
logo = pygame.image.load('images/logo.png')
setup = pygame.image.load('images/setup.png')
pygame.display.set_caption('clicked on image')

key = pygame.key.get_pressed()
clock = pygame.time.Clock()
buttons = []

class Window():
    def __init__(self, screen, position, size):
        self.screen = screen
        self.rect = Rect(position, size)


class Button():
    def __init__(self, parent, position, size, color, callback_function):

        self.parent = parent
        self.position = position
        self.size = size
        self.color = color
        self.callback = callback_function
        self.screen = parent.screen
        self.rect = Rect(position, size)

    def get_event(self, event):
        #if self.rect.collidepoint(event.pos):
        #screen.fill((255, 255, 255))
        pygame.display.update()
        self.callback()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def create_button():
    newwindow = Window(screen, (10, 10), SCREEN_SIZE)
    newbutton = Button(newwindow, (150, 250), (100, 50), pygame.Color('Pink'), test_button_event)
    buttons.append(newbutton)
    newbutton.draw()

def test_button_event():
    screen.blit(logo, (10, 0))
    screen.fill((255, 255, 255))
    pygame.display.flip()

#Main Loop
create_button()



while True:

    screen = pygame.display.set_mode(SCREEN_SIZE, 32)
    # screen.fill((255, 255, 255))
    # screen.blit(bg, (0, 0))
    # screen.blit(logo, (10, 0))
    screen.blit(snap, (10, 190))
    screen.blit(setup, (470, 470))
    for button in buttons:
        button.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)

    mouse = pygame.mouse.get_pos()

    if event.type == MOUSEBUTTONDOWN and 150+100 > mouse[0] > 150 and 250+50 > mouse[1] > 250:

        print("mouse at (%d, %d)" % event.pos)
        button.get_event(event)

    pygame.display.update()
