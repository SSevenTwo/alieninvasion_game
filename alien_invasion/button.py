import pygame.font

class Button():
    """Class for creating buttons"""
    
    def __init__(self,settings,screen,message):
        """Initializes button attributes"""
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        
        #Dimensions of the buttton
        self.width = 200
        self.height = 50
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #Button's rect
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #Creating the button image
        self.prep_msg(message)
        
    def prep_msg(self, msg):
        """Turns message into a rendered image"""
        #The true is for anti aliasing. Can add an extra argument after for highlight color.
        self.image = self.font.render(msg,True,self.text_color)
        #We must first create a rect for the image, then we modify it
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center
        
    def draw_button(self):
        """Draws the button on the screen"""
        #The first line is to make the square of the button.
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.image,self.image_rect)
        
