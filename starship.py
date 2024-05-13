import pygame


class Ship():
#Initialization of ship
    def __init__(self, screen): 
        self.screen = screen
        self.image = pygame.image.load('images/starshippy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.speed = 8
        self.last_shot =pygame.time.get_ticks()


    def draw_ship(self):
    #Draw the ship
        self.screen.blit(self.image, self.rect)

    
    def update_ship(self):
    #Update the position of ship
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.mleft and self.rect.left > 0:
            self.center -= self.speed
        self.rect.centerx = self.center

    
    def create_ship(self):
    #Create ship in the center
        self.center = self.screen_rect.centerx