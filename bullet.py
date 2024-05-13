import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, ship):
    #Initialization of bullet
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 20)
        self.color = 255, 0, 0
        self.speed = 17
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.rect.y = float(self.rect.y)

    
    
    def update(self):
    #Movement of bullet to upper side    
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
        
    
    
    def draw_bullet(self):
    #Draw the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)