import pygame
import sys
from bullet import Bullet
from alien import Alien
from explosion import Explosion
#from sounds import *


def events(screen, ship, bullets, time_now, cooldown):
#Analysis of events
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_d:
                    ship.mright = True
               elif event.key == pygame.K_a:
                    ship.mleft = True
               elif event.key == pygame.K_SPACE and time_now - ship.last_shot > cooldown:
                    #bullet_sound.play()
                    newbullet = Bullet(screen, ship)
                    bullets.add(newbullet)
                    ship.last_shot = time_now
          elif event.type == pygame.KEYUP:
               if event.key == pygame.K_d:
                    ship.mright = False
               elif event.key == pygame.K_a:
                    ship.mleft = False


def update(screen, sc, ship, aliens, explosion_group, bullets): #add bg for static image and make screen blit 
#Update of screen
     #screen.blit(bg, (0, 0))
     sc.show_score()
     for bullet in bullets.sprites():
          bullet.draw_bullet()
     ship.draw_ship()
     aliens.draw(screen)
     explosion_group.draw(screen)
     pygame.display.flip()



def update_bullets(screen, stats, sc, aliens, explosion_group, bullets):
#Update position of bullets
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
     collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
     if collisions:
          explosion = Explosion(bullet.rect.centerx, bullet.rect.y, 2)
          explosion_group.add(explosion)
          for aliens in collisions.values():
               stats.score += 10 * len(aliens)
          sc.image_score()
          sc.image_healthm()
     if len(aliens) == 0:
          bullets.empty()
          create_army(screen, aliens)




def increasement_aliens(stats, sc, aliens):
     if stats.ship_left == 3 or stats.ship_left == 2 or stats.ship_left ==1:
          if sc.stats.score >= 1120:
               for alien in aliens.sprites():
                    alien.speed = 0.25
          if sc.stats.score >= 2240:
               for alien in aliens.sprites():
                    alien.speed = 0.3
          if sc.stats.score >= 3360:
               for alien in aliens.sprites():
                    alien.speed = 0.35




def ship_kill(stats, screen, sc, ship, aliens, bullets, text1, text2):
#Kick between army and ship
     if stats.ship_left > 1:
          stats.ship_left -= 1
          sc.image_healthm()
          aliens.empty()
          bullets.empty()
          create_army(screen, aliens)
          ship.create_ship()
     else:
          for x in range(-4, 5):
               for y in range(-4, 5):
                    screen.blit(text2, (175 + x, 325 + y))
          screen.blit(text1, (175, 325))
          pygame.display.flip()
          stats.run_game = False
          #sys.exit()


def update_aliens(stats, screen, sc, ship, aliens, bullets, explosion_group, text1, text2):
#Update position of aliens
     aliens.update()
     if pygame.sprite.spritecollideany(ship, aliens):
          explosion = Explosion(ship.rect.centerx, ship.rect.centery, 3)
          explosion_group.add(explosion)
          ship_kill(stats, screen, sc, ship, aliens, bullets, text1, text2)
     aliens_check(stats, screen, sc, ship, aliens, bullets, text1, text2)


def aliens_check(stats, screen, sc, ship, aliens, bullets, text1, text2):
#Check if the army touched the edge
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
          if alien.rect.bottom >= screen_rect.bottom:
               ship_kill(stats, screen, sc, ship, aliens, bullets, text1, text2)
               break


def create_army(screen, aliens):
#Creating the army     
     alien = Alien(screen)
     alien_width = alien.rect.width
     number_alien_x = int((800 - 2 * alien_width) / alien_width)
     alien_height = 1.5 * alien.rect.height
     number_alien_y = int((800 - 100 - alien_height) / alien_height)
     alien.speed += 1


     for row_number in range(number_alien_y - 1):
          for alien_number in range(number_alien_x):
               alien = Alien(screen)
               alien.x = alien_width + (alien_width * alien_number)
               alien.y = alien_height + (alien_height * row_number)
               alien.rect.x = alien.x
               alien.rect.y = alien.rect.height + alien.rect.height * row_number
               aliens.add(alien)


def update_explosion_group(explosion_group):
#Update position of explosions
     explosion_group.update()