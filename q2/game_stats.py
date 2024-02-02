
class Game_Stats:
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = True
        
    def reset_stats(self):
        self.player_lives_left = self.settings.player_lives_left
        