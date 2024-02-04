import pygame
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self, screen, settings):
        super(Player, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/player.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # initial position of a player : screen center
        
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery
        
        # center position of the player
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        
        #motion direction
        
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    
    #movement of the player
    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.settings.player_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.settings.player_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x +=self.settings.player_speed_factor
            
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center_x -= self.settings.player_speed_factor
            
        
        self.center_player()
        

    #draw player on the screen
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
        
    def center_player(self):
        self.rect.centerx = self.center_x
        self.rect.centery= self.center_y
        
        
    