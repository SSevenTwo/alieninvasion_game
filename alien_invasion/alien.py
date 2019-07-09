import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class which represents the aliens in the game"""
    
    def __init__(self,settings,screen):
        """Creates alien object"""
        super(Alien,self)
        self.screen = screen
        self.settings = settings
        
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store exact position as a float
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw alien"""
        self.screen.blit(self.image,self.rect)
