import pygame
from pygame.sprite import Sprite


class Health(Sprite):
#Initialization of health
    def __init__(self, screen): 
        super(Health, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Healthpy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()   