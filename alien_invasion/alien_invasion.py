import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():
    """"Initializes the game"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(settings)
    
    #Makes a ship/alien object and bullet group
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Creat aliens
    g.create_army(settings,screen,ship,aliens)
    
    #Start main loop of the game.
    while True:
        
        #Watch for game events and moves ship
        g.update_events(settings,screen,ship,bullets)
        
        if stats.game_active:
            ship.move()
            g.update_bullets(settings,screen,ship,aliens,bullets)
            g.update_aliens(settings, stats, screen, ship, aliens,bullets)
        
        #Updates screen after each loop
        g.update_screen(settings, screen, ship, aliens, bullets)

run_game()
