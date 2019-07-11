class Settings():
    """Stores the settings of the game"""
    
    def __init__(self):
        """Ïnitialize static game settings"""
        self.screen_width = 1360
        self.screen_height = 768
        self.bg_color = (230,230,230)
        self.ship_lives = 2
    
        #Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_limit = 3
        
        #Alien settings
        self.alien_drop_speed = 50
        
        #Sets dynamic settings
        self.dynamic_settings_reset()
        self.speedup_multiplier = 1.1
        
    def dynamic_settings_reset(self):
        """Sets the dynamic settings to a default starting value"""
        #Ship and bullet settings
        self.bullet_speed = 3
        self.ship_speed = 3
        
        #Alien settings
        self.alien_speed = 0.5
        #1 represents moving right, -1 represents moving left
        self.alien_direction = 1
        
    def increase_speed(self):
        """Increases the speed of the game by the multiplier"""
        self.bullet_speed *= self.speedup_multiplier
        self.ship_speed *= self.speedup_multiplier
        self.alien_speed *= self.speedup_multiplier
        
