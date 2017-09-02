import os
import pygame
import sys
class PaintEvent:
    def __init__(self,func,screen, mouse, mat, i):
        self.func=func
        self.screen=screen
        self.mouse=mouse
        self.mat=mat
        self.i=i
    def start(self):
        self.func(self.screen,self.mouse,self.mat,self.i)
class EventSystem:
    gameEvent=None
    def __init__(self):
        pass
    def setEvent(self,gameEvent,USEREVENT_ARRAY):
        self.gameEvent = gameEvent
        self.USEREVENT_ARRAY = USEREVENT_ARRAY
    def mainevent(self,mat,i):
        for event in self.gameEvent:
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type== pygame.MOUSEBUTTONDOWN:
                self.mousePressDown()
            elif event.type==self.USEREVENT_ARRAY[0]:
                self.paint_event.start()

    def paintEvent(self,func,screen, mouse, mat, i):
        self.paint_event=PaintEvent(func,screen,mouse,mat,i)
        self.mat=mat
        self.i=i
    def quit(self):
        pygame.quit()
        sys.exit()
    def mousePressDown(self):
        pressed_array = pygame.mouse.get_pressed()
        for m_botton in pressed_array:
            if pressed_array[m_botton]:
                if m_botton == 0:
                    # left
                    # print "Left"
                    pos = pygame.mouse.get_pos()
                    if pos[0]>self.mat[self.i][0] and pos[1]>self.mat[self.i][1] and pos[0]<self.mat[self.i][0]+300 and pos[1]<self.mat[self.i][1]+300:
                        print "press"
                    #print pos[0]
                    #print self.mat[0][0]
                elif m_botton == 1:
                    pass
                    # weel
                    # print "Weel"
                elif m_botton == 2:
                    pass
                    # right
                    # print "Right"
