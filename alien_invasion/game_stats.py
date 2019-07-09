class GameStats():
    """Tracks the games progress and stats"""
    
    def __init__(self,settings):
        """Initializes the game stats object"""
        self.settings = settings
        self.reset_stats()
        #Game only begins/continues if True
        self.game_active = True
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_lives
