class Settings():
    """Stores the settings of the game"""
    
    def __init__(self):
        """Ïnitialize game settings"""
        self.screen_width = 1360
        self.screen_height = 768
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        
        #Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_limit = 3
        
        #Alien settings
        self.alien_speed = 1
        self.alien_drop_speed = 10
        #1 represents moving right, -1 represents moving left
        self.alien_direction = 1
