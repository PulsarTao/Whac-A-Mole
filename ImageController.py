import pygame


class Mouse():
    def __init__(self,filename):
        self.surface = pygame.Surface((300, 300))
        self.surface.blit(pygame.image.load(filename).convert_alpha(), (0, 0), (0, 0, self.surface.get_width(), self.surface.get_height()))
        self.rect=self.surface.get_rect()
    def get_rect(self):
        return self.rect