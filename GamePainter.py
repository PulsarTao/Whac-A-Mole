import pygame
from pygame.locals import *
#
#
#
#
#


class GamePainter:
    def __init__(self):
        pass
    def paint(self,screen,mouse, mat,i):
            screen.blit(mouse.surface, mat[i])
            #pygame.time.delay(1000)
            pygame.display.update()
    def createMartix(self):
        pass
