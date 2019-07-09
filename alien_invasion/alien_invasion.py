import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g
from pygame.sprite import Group
from alien import Alien

def run_game():
    """"Initializes the game"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Makes a ship/alien object and bullet group
    ship = Ship(settings, screen)
    bullets = Group()
    alien = Alien(settings,screen)
    
    #Start main loop of the game.
    while True:
        
        #Watch for game events and moves ship
        g.update_events(settings,screen,ship,bullets)
        ship.move()
        g.update_bullets(bullets)
        
        #Updates screen after each loop
        g.update_screen(settings, screen, ship, alien, bullets)

run_game()