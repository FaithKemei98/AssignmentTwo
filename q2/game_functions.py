import sys
import pygame
from projectile import Projectile
from enemy import Enemy
from collectible import Collectible
from time import sleep


def check_events(settings, screen,player, projectiles):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings, screen, player, projectiles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def check_keydown_events(event,settings, screen, player, projectiles):
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
    if event.key == pygame.K_SPACE:
        shoot_projectile(settings, screen, player,projectiles)
        
def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        
    if event.key == pygame.K_LEFT:
        player.moving_left = False 
    if event.key == pygame.K_UP:
        player.moving_up = False 
    if event.key == pygame.K_DOWN:
        player.moving_down = False 

def shoot_projectile(settings, screen, player,projectiles):
    new_projectile = Projectile(settings,screen, player)
    projectiles.add(new_projectile)
    
def update_projectile(projectiles, enemies):
    projectiles.update(projectiles, enemies)
    #deleting bullets that are off the screen
    for proj in projectiles.copy():
        if proj.rect.bottom <=0:
            projectiles.remove(proj) 
    
    #detecting collision between projectile and an enemy
        check_projectile_enemy_collision(projectiles, enemies)

def check_projectile_enemy_collision(projectiles, enemies):
    collision = pygame.sprite.groupcollide(projectiles, enemies, True, True)
            
        
def update_screen(screen, settings, player,projectiles,enemy, collectibles):
    screen.fill(settings.bg_color)
    for proj in projectiles.sprites():
        proj.draw_projectile()
    player.update()
    player.blit_me()
    enemy.update()
    enemy.draw(screen)
    collectibles.draw(screen)
    

def create_enemies(screen, settings, enemies):
    enemies_number = settings.enemies_number
    
    for enem_num in range(enemies_number):
        enemy = Enemy(settings, screen)
        enemies.add(enemy)
        

def create_collectibles(screen, settings, collectibles):
    collectibles_num = settings.collectible_num
    for i in range(collectibles_num):
        collectible = Collectible(screen,settings)
        collectibles.add(collectible)

def update_enemy( screen,settings,enemies, player, stats, projectiles):
    if pygame.sprite.spritecollideany(player, enemies):
        player_hit(screen,settings,enemies,player, stats, projectiles)
        

def player_hit(screen, settings, enemies, player, stats, projectiles):
    if stats.player_lives_left > 0:
        
        #decreament the life of a player
        stats.player_lives_left -=1
        
        #clear all the projectiles and enemies
        projectiles.empty()
        enemies.empty()
        
        
        #create a set of enemies
        create_enemies(screen,settings,enemies)
        
        #center the player
        player.center_player()
        
        #pause the game for half a second
        sleep(0.5)
    
    else:
        stats.game_active = False
    