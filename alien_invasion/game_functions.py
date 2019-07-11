import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from filehandling import save_score

def update_events(settings, screen, stats, play_button, ship,aliens,bullets,scoreboard):
    """Respond to game events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(stats)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown(event, settings, screen, ship, bullets,stats)
            elif event.type == pygame.KEYUP:
                check_keyup(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Names the 2 numbers in the tuple x and y
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #mouse_y = pygame.mouse.get_pos()
                check_play_button(settings, screen, stats,play_button,mouse_x,mouse_y,ship,aliens,bullets,scoreboard)

def update_screen(settings, screen, stats, scoreboard, ship, aliens, bullets,play_button):
    """Updates the screen"""
    #Re-draw the screen
    screen.fill(settings.bg_color)
    
    #Draws bullets and ship
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    scoreboard.show_score()
    
    if not stats.game_active:
        play_button.draw_button()
        
    #Draw the latest screen
    pygame.display.flip()
    
def check_keydown(event, settings, screen, ship, bullets, stats):
    """Checks when a key is being pressed"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        shoot_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        save_score(stats)
        sys.exit()
        
def check_keyup(event, ship):
    """Checks when a key is being released"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

def update_bullets(settings,screen,stats,scoreboard,ship, aliens,bullets):
    """Updates position of bullets as well as delete old bullets"""
    bullets.update()
    bullet_alien_collision(settings,screen,stats,scoreboard, ship,aliens,bullets)
        
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
    
    #Creates rows of aliens
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
    
def update_aliens(settings,stats, screen,ship,aliens,bullets,scoreboard):
    """Update position of aliens"""
    check_army_position(settings,aliens)
    aliens.update()
    
    #look for ship and alien collisions
    #This method is different in that it checks collision of a sprite and a group.
    #The other method checked collision of groups
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(settings,stats,screen,ship,aliens,bullets,scoreboard)
        
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, scoreboard)
    
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
    
def bullet_alien_collision(settings,screen,stats,scoreboard, ship,aliens,bullets):
    """Checks whether bullet collides with alien. If so delete both."""
    #This returns a dictionary of the first argument as a key and the 2nd as a value
    #The first true means delete bullet, and 2nd on is the alien.
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    #Determines how many aliens were hit with the bullet (incase bullet hits more than 1)
    count = sum(len(v) for v in collisions.values())
    
    if collisions:
        stats.score += (settings.points_earned * count)
        scoreboard.prep_score()
        check_highscore(stats,scoreboard)
    
    #Make a new army if the current one is all dead and speed up the game.
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        scoreboard.prep_level()
        create_army(settings,screen,ship,aliens)
        
def ship_hit(settings,stats,screen,ship,aliens,bullets,scoreboard):
    """Response to alien hitting the ship"""
    if stats.ships_left > 0:
        
        stats.ships_left -= 1
        scoreboard.prep_ships()
    
        #Removes all bullets and aliens to reset game
        aliens.empty()
        bullets.empty()
    
        #Make new army and center the ship
        create_army(settings, screen, ship, aliens)
        ship.center_ship()
    
        #Pause to let the user see the collision
        sleep(0.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets,scoreboard):
    """Check if any aliens have hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings,stats,screen,ship,aliens,bullets,scoreboard)
            break
            
def check_play_button(settings, screen, stats,play_button,mouse_x,mouse_y,ship,aliens,bullets,sb):
    """Starts game if button is clicked on"""
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        #Hide mouse while in game
        pygame.mouse.set_visible(False)
        settings.dynamic_settings_reset()
        stats.reset_stats()
        
        #Reset scoreboard
        sb.prep_score()
        sb.prep_highscore()
        sb.prep_level()
        sb.prep_ships()
        
        stats.game_active = True
        
        #Resets the game state
        bullets.empty()
        aliens.empty()
        create_army(settings,screen,ship,aliens)
        ship.center_ship()
        
def check_highscore(stats,scoreboard):
    """Checks whether a highscore has been set"""
    if stats.score > stats.highscore:
        stats.highscore = stats.score
        scoreboard.prep_highscore()
        
