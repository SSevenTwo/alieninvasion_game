import pygame
from settings import Settings

class Ship():
    
    def __init__(self,settings,screen):
        """Initialize screen and starting position of ship"""
        self.screen = screen
        
        #load ship image and rect properties
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #position ship at the bottom and centered
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #movement flags
        self.move_right = False
        self.move_left = False
        
        #Ship positiona as float
        self.position = float(self.rect.centerx)
        
        #Store settings
        self.settings = settings
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
        
    def move(self):
        """Updates the position of the ship and limits it within the screen"""
        if self.move_right and self.rect.centerx < self.screen_rect.right:
            self.position += self.settings.ship_speed
        if self.move_left and self.rect.centerx > 0:
            self.position -= self.settings.ship_speed
            
        self.rect.centerx = self.position
        
    def center_ship(self):
        """Resets the ship to the center"""
        self.center = self.screen_rect.centerx
        
    
