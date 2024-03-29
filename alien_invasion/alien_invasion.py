import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as g
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import filehandling as f

def run_game():
    """"Initializes the game"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(settings)
    scoreboard = Scoreboard(settings,screen,stats)
    f.load_score(stats,scoreboard)
    
    #Play button
    play_button = Button(settings,screen,"Play")
    
    #Makes a ship/alien object and bullet group
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Creat aliens
    g.create_army(settings,screen,ship,aliens)
    
    #Start main loop of the game.
    while True:
        
        #Watch for game events and moves ship
        g.update_events(settings,screen,stats,play_button,ship,aliens,bullets,scoreboard)
        
        if stats.game_active:
            ship.move()
            g.update_bullets(settings,screen,stats,scoreboard,ship, aliens,bullets)
            g.update_aliens(settings, stats, screen, ship, aliens,bullets,scoreboard)
        
        #Updates screen after each loop
        g.update_screen(settings, screen, stats,scoreboard, ship, aliens, bullets,play_button)

run_game()
