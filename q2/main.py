import pygame
from settings import Settings
import game_functions as gf
from player import Player
from pygame.sprite import Group
from collectible import Collectible

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
    
    gf.create_enemies(screen,settings,enemies)
    
    gf.create_collectibles(screen, settings, collectibles)
    
    while True:
        
        gf.check_events(settings, screen, player,projectiles)
        gf.update_projectile(projectiles, enemies)
        gf.update_enemy(enemies, player)
        gf.update_screen(screen, settings, player, projectiles, enemies, collectibles)
        
        
        pygame.display.flip()

run_game()