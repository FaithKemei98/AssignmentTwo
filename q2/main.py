import pygame
from settings import Settings
import game_functions as gf
from player import Player

def run_game():
    #settings instance
    settings = Settings()
    
    pygame.init()
    screen = pygame.display.set_mode((settings.window_width,settings.window_height))
    pygame.display.set_caption("Game")
    
    # player instance
    player = Player(screen, settings)
    
    screen.fill(settings.bg_color)
    
    while True:
        gf.check_events(player)
        player.movement()
        gf.update_screen(player)
        pygame.display.flip()

run_game()