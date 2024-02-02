import pygame
from settings import Settings
import game_functions as gf
from player import Player
from pygame.sprite import Group
from game_stats import Game_Stats

def run_game():
    #settings instance
    settings = Settings()
    
    pygame.init()
    screen = pygame.display.set_mode((settings.window_width,settings.window_height))
    pygame.display.set_caption("Game")
    
    # player instance
    player = Player(screen, settings)
    
    #creating a list of projectiles
    projectiles = Group()
    
    #list of enemies
    enemies = Group()
    
    #list of collectiles
    collectibles = Group()
    
    #instance of a game_stats
    game_stats = Game_Stats(settings)
    
    gf.create_enemies(screen,settings,enemies)
    
    gf.create_collectibles(screen, settings, collectibles)
    
    while True:
        
        gf.check_events(settings, screen, player,projectiles)
        #making sure game is played when player has more than one life
        if game_stats.game_active:
            gf.update_projectile(projectiles, enemies)
            gf.update_enemy(screen,settings,enemies, player, game_stats, projectiles)
            gf.update_screen(screen, settings, player, projectiles, enemies, collectibles)
            pygame.display.flip()

run_game()