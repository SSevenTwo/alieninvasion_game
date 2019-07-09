import sys
import pygame
from bullet import Bullet

def update_events(settings, screen, ship,bullets):
    """Respond to game events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown(event, settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup(event, ship)
                
                

def update_screen(settings, screen, ship, alien, bullets):
    """Updates the screen"""
    #Re-draw the screen
    screen.fill(settings.bg_color)
    
    #Draws bullets and ship
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
        
    #Draw the latest screen
    pygame.display.flip()
    
def check_keydown(event, settings, screen, ship, bullets):
    """Checks when a key is being pressed"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        shoot_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

        
def check_keyup(event, ship):
    """Checks when a key is being released"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

def update_bullets(bullets):
    """Updates position of bullets as well as delete old bullets"""
    bullets.update()
        
    #Remove bullets when top is reached
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
                bullets.remove(bullet)

def shoot_bullet(settings, screen, ship, bullets):
    """Shoots a bullet if the limit is not reached"""
    if len(bullets) < settings.bullet_limit:
        bullet = Bullet(settings,screen,ship)
        bullets.add(bullet)
    
