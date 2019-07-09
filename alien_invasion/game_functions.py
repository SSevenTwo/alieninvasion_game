import sys
import pygame
from bullet import Bullet
from alien import Alien

def update_events(settings, screen, ship,bullets):
    """Respond to game events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown(event, settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup(event, ship)

def update_screen(settings, screen, ship, aliens, bullets):
    """Updates the screen"""
    #Re-draw the screen
    screen.fill(settings.bg_color)
    
    #Draws bullets and ship
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
        
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
        
def create_army(settings, screen, ship, aliens):
    """Creates an army of aliens"""
    #Uses an alien to determine how many aliens can fit on the screen
    alien = Alien(settings,screen)
    number_of_aliens = get_alien_no(settings,alien.rect.width)
    number_of_rows = get_number_rows(settings,ship.rect.height,alien.rect.height)
    
    
    #Creates row of aliens
    for row_number in range(number_of_rows):
        for alien_no in range(number_of_aliens):
            create_alien(settings,screen,aliens,alien_no, row_number)
        
def create_alien(settings,screen,aliens,alien_no, row_number):
    """Creates aliens for the alien army"""
    alien = Alien(settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_no)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def get_alien_no(settings,alien_width):
    """Determins the number of aliens in a row"""
    screen_width = settings.screen_width - (2*alien_width)
    number_of_aliens = int(screen_width / (2*alien_width))
    return number_of_aliens
    
def get_number_rows(settings,ship_height,alien_height):
    """Determins how many rows of aliens to spawn"""
    screen_height = settings.screen_height - (3*alien_height) - ship_height
    number_of_rows = int(screen_height/(2*alien_height))
    return number_of_rows
    
def update_aliens(settings,aliens):
    """Update position of aliens"""
    check_army_position(settings,aliens)
    aliens.update()
    
def check_army_position(settings,aliens):
    """Checks whether the army has hit the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edge_hit():
            change_army_direction(settings,aliens)
            break
             
def change_army_direction(settings,aliens):
    """Moves aliens down and reverses direction"""
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed
    settings.alien_direction *= -1
    
  
    
