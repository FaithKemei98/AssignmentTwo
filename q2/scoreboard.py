import pygame.font
import pygame
from pygame.sprite import Group
from player import Player

class ScoreBoard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.settings = settings
        self.stats = stats
        
        self.screen_rect = self.screen.get_rect()
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        #prepare the initial score
        self.prep_score()
        self.prep_players()
        
    def prep_players(self):
        self.players = Group()
        for player_num in range(self.settings.player_lives_left):
            player = Player(self.screen, self.settings)
            player.rect.x = 10 + player_num * player.rect.width
            player.rect.top = 10
            self.players.add(player)
        
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #positioning the score at the top right cornner
        
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right -20
        self.score_image_rect.top = 20
    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.players.draw(self.screen)
        
    
        