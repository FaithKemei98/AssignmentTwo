import pygame
from settings import Settings
import game_functions as gf
from player import Player
from pygame.sprite import Group

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
    
    #enemy instance
    enemies = Group()
    
    gf.create_enemies(screen,settings,enemies)
    
    while True:
        
        gf.check_events(settings, screen, player,projectiles)
        gf.update_projectile(projectiles, enemies)
        gf.update_screen(screen, settings, player, projectiles, enemies)
        
        
        pygame.display.flip()

run_game()