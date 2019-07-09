import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class that represents the bullets shot from the ship"""
    
    def __init__(self,settings,screen,ship):
        """Creates the bullets at the ship's position"""
        
        super(Bullet,self).__init__()
        self.screen = screen
        
        #Drawing a bullet
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Convert bullet position to float
        self.y = float(self.rect.y)
        
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        """Move bullet"""
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draws bullet on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
