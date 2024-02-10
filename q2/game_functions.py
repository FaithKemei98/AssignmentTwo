import sys
import pygame
from projectile import Projectile
from enemy import Enemy
from collectible import Collectible
from time import sleep


def check_events(settings, screen,player, projectiles, stats, play_button,enemies, score_board):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings, screen, player, projectiles)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, player)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y,projectiles, enemies, player, screen, settings,score_board)
        

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

def check_play_button(stats, play_button, mouse_x, mouse_y, projectiles, enemies, player, screen, settings, score_board):
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        
        #restore the game settings attr
        settings.initialize_dynamic_attr()
        #hide mouse on top of play button
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        
        #clear all enemies and projectiles
        projectiles.empty()
        enemies.empty()
        
        #create a new list of enemies and center the pplayer
        create_enemies(screen,settings,enemies)
        player.center_player()
        score_board.prep_players()
        
        
        
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
    
def update_projectile(projectiles, enemies,settings,screen,stats,score_board):
    projectiles.update(projectiles, enemies)
    #deleting bullets that are off the screen
    for proj in projectiles.copy():
        if proj.rect.bottom <=0:
            projectiles.remove(proj) 
    
    #detecting collision between projectile and an enemy
        check_projectile_enemy_collision(projectiles, enemies,settings,screen,stats,score_board)

def check_projectile_enemy_collision(projectiles, enemies, settings,screen, stats,score_board):
    collision = pygame.sprite.groupcollide(projectiles, enemies, True, True)
    
    if collision:
        stats.score += settings.enemy_hit_points
        score_board.prep_score()
    
    if len(enemies)==0:
        projectiles.empty()
        settings.increase_speed()
        stats.level +=1
        score_board.prep_level()
        create_enemies(screen,settings, enemies)

def check_player_collectible_collision(screen,player, collectible, settings, stats):
    collision = pygame.sprite.spritecollide(player, collectible, True)
    if collision:
        stats.player_lives_left +=2
        
        create_collectibles(screen,settings, collectible)
        
    
        
            
        
def update_screen(screen, settings, player,projectiles,enemy,stats, collectibles, play_button, score_board, screen_rect):
    screen.fill(settings.bg_color)
    if not stats.game_active or stats.player_lives_left <=0:
        play_button.draw_button()
    
    else:
    
        for proj in projectiles.sprites():
            proj.draw_projectile()
        player.update()
        player.blit_me()
        enemy.update()
        enemy.draw(screen)
        collectibles.draw(screen)
        score_board.show_score()
        score_board.prep_players()
        update_enemy(screen,settings,enemy,player,stats,projectiles, score_board, screen_rect)
        check_player_collectible_collision(screen,player, collectibles, settings,stats)
        delete_enemy_hit_bottom(screen, settings, enemy, screen_rect, player, stats, projectiles, score_board)
        
    pygame.display.flip()
    

def delete_enemy_hit_bottom(screen, settings, enemies, screen_rect, player, stats, projectiles, score_board):
    for enem in enemies.sprites():
        if enem.rect.top >= screen_rect.bottom:
            enemies.remove(enem)
            player_hit(screen, settings, enemies, player, stats, projectiles, score_board)
    
    if len(enemies)==0:
        create_enemies(screen,settings,enemies)
    

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

def update_enemy( screen,settings,enemies, player, stats, projectiles, score_board, screen_rect):
    if pygame.sprite.spritecollideany(player, enemies):
        player_hit(screen,settings,enemies,player, stats, projectiles, score_board)
        
        #delete_enemy_hit_bottom(screen, settings, enemies,screen_rect, player,  stats, projectiles, score_board)
        

def player_hit(screen, settings, enemies, player, stats, projectiles, score_board):
    if stats.player_lives_left > 0:
        
        #decreament the life of a player
        stats.player_lives_left -=1
        
        score_board.prep_players()
        
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
        pygame.mouse.set_visible(True)
    