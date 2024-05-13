import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen):
    #Initialization of alien
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alienforpy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.2

    
    
    def draw(self):
    #Draw the alien
        self.screen.blit(self.image, self.rect)
    
    
    def update(self):
    #Movement af aliens
        self.y += self.speed
        self.rect.y = self.y