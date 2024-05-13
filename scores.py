import pygame.font
from health import Health
from pygame.sprite import Group

class Scores():
#Show ingame information    
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 255, 255)
        self.font = pygame.font.SysFont('impact', 50)
        self.outline_color = (0, 0, 0)
        self.outline_font = pygame.font.SysFont('impact', 50)
        self.image_score()
        self.image_healthm()

    def image_score(self):
    #Make text of score into graphic image
        self.score_img = self.font.render((f'score: {str(self.stats.score)}'), True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 15
        self.score_img1 = self.outline_font.render((f'score: {str(self.stats.score)}'), True, self.outline_color)
        self.score_rect1 = self.score_img1.get_rect()
        self.score_rect1.right = self.screen_rect.right - 30
        self.score_rect1.top = 15
    
    def image_healthm(self):
    #Number of health
        self.healthm = Group()
        for health_number in range(self.stats.ship_left):
            health = Health(self.screen)
            health.rect.x = 15 + health_number * health.rect.width
            health.rect.y = 20
            self.healthm.add(health)


    def show_score(self):
    #Show the score into the screen
        for x in range(-3, 4):
               for y in range(-3, 4):
                    self.screen.blit(self.score_img1, (self.score_rect.x + x, self.score_rect.y + y))
        self.screen.blit(self.score_img, self.score_rect)
        self.healthm.draw(self.screen)