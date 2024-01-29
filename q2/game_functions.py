import sys
import pygame

def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def check_keydown_events(event, player):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    if event.key == pygame.K_LEFT:
        player.moving_left = True
    if event.key == pygame.K_UP:
        player.moving_up = True
    if event.key == pygame.K_DOWN:
        player.moving_down = True
        
def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        
    if event.key == pygame.K_LEFT:
        player.moving_left = False 
    if event.key == pygame.K_UP:
        player.moving_up = False 
    if event.key == pygame.K_DOWN:
        player.moving_down = False 
        
def update_screen(player):
    player.blit_me()