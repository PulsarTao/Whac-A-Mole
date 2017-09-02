import random
import sys
import pygame
from pygame.locals import *
#from GamePainter import GamePainter
from pygame.threads import Thread
from time import sleep

from EventSystem import EventSystem
from GamePainter import GamePainter
from ImageController import Mouse
def play():
    pygame.init()
    window_size = (width, height) =(600, 600)
    speed=10
    color_black = (0, 0, 139)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Mouse')
    mouse=Mouse("mouse.jpg")
    mouse_rect =mouse.get_rect()
    painter=GamePainter()
    mat=[
        [0,0],
        [300,0],
        [0,300],
        [300,300]
         ]
    SPAWNASTEROID = USEREVENT + 1
    USEREVENT_ARRAY=[]
    USEREVENT_ARRAY.append(SPAWNASTEROID)
    pygame.time.set_timer(SPAWNASTEROID, 1000)
    event=EventSystem()
    while True:
        i=random.randint(0,3)
        screen.fill(color_black)
        event.setEvent(pygame.event.get(),USEREVENT_ARRAY)
        event.paintEvent(painter.paint,screen,mouse, mat, i)
        event.mainevent(mat,i)