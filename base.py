import pygame
import control
from starship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    screen = pygame.display.set_mode((800, 800)) #pygame.RESIZABLE
    pygame.display.set_caption('Cosmic raider')
    bg = pygame.image.load('images/space1.png')
    bg = pygame.transform.scale(bg, (800, 800))
    bg_y = 0 #del for static
    ship = Ship(screen)
    bullets = Group() 
    aliens = Group()
    explosion_group = Group()
    control.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)
    font30 = pygame.font.SysFont('impact', 100)
    text1 = font30.render('GAME OVER', True, (255, 255, 255))
    text2 = font30.render('GAME OVER', True, (0, 0, 0))
    


    


    while True:
    #Main cycle of game
        clock.tick(fps)
        time_now = pygame.time.get_ticks()
        cooldown = 100
        control.events(screen, ship, bullets, time_now, cooldown)
        if stats.run_game:
            ship.update_ship()
            bullets.update()
            aliens.update()
            control.increasement_aliens(stats, sc, aliens)
            control.update(screen, sc, ship, aliens, explosion_group, bullets) #add bg for static image
            control.update_bullets(screen, stats, sc, aliens, explosion_group, bullets)
            control.update_aliens(stats, screen, sc, ship, aliens, bullets, explosion_group, text1, text2)
            control.update_explosion_group(explosion_group)
            screen.blit(bg, (0, bg_y)) #del for static
            screen.blit(bg, (0, bg_y - 800)) #del for static
            bg_y += 1 #del for static
            if bg_y >= 800: #del for static
                bg_y = 0 #del for static 


run()