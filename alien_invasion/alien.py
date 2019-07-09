import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class which represents the aliens in the game"""
    
    def __init__(self,settings,screen):
        """Creates alien object"""
        super(Alien,self).__init__()
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
        
    def update(self):
        """Move alien"""
        self.x += (self.settings.alien_speed * self.settings.alien_direction)
        self.rect.x = self.x
    
    def check_edge_hit(self):
        """Checks whether the alien has hit the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
