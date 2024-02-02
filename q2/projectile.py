import pygame
from pygame.sprite import Sprite
class Projectile(Sprite):
    def __init__(self, settings, screen, player):
        super(Projectile,self).__init__()
        self.screen = screen
        self.color = settings.projectile_color
        self.speed_factor = settings.projectile_speed_factor
        
        #create a projectile
        self.rect = pygame.Rect(0,0, settings.projectile_width, settings.projectile_hight)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        
        #projectile position as a decimal value
        
        self.y = float(self.rect.y)
        
    #function to move the projectile.
    def update(self, projectiles, enemies):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
        #detecting collision between projectile and an enemy
        collision = pygame.sprite.groupcollide(projectiles, enemies, True, True)
    
    #drawing the projectile on the screen
    def draw_projectile(self):
        pygame.draw.rect(self.screen,self.color,self.rect)