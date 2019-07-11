import pygame.font

class Scoreboard():
    """Class responsible for desplaying the scores"""
    
    def __init__(self, settings,screen,stats):
        """Initialize score attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.settings = settings
        
        #Font settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        
        #Create initial score image
        self.prep_score()
        self.prep_highscore()
        
    def prep_score(self):
        """Creates rendered image of the score"""
        rounded_score = int(round(self.stats.score,-1))
        str_score = "{:,}".format(rounded_score)
        self.image = self.font.render(str_score,True,self.text_color)
        
        self.image_rect = self.image.get_rect()
        self.image_rect.right = self.screen_rect.right - 20
        self.image_rect.top = 20
        
    def show_score(self):
        """Draws score onto the screen"""
        self.screen.blit(self.image,self.image_rect)
        self.screen.blit(self.highscore,self.highscore_rect)
        
    def prep_highscore(self):
        """Creates rendered image of the highscore"""
        rounded_score = int(round(self.settings.highscore,-1))
        str_score = "{:,}".format(rounded_score)
        self.highscore = self.font.render(str_score,True,self.text_color)
        
        self.highscore_rect = self.highscore.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = 20
        
        
