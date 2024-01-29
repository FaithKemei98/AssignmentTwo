import pygame

class Player:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # initial position of a player : bottom center
        
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
    def movement(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.settings.move_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.settings.move_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x +=self.settings.move_speed_factor
            
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center_x -= self.settings.move_speed_factor
            
        self.rect.centerx = self.center_x
        self.rect.centery= self.center_y
            
        

    #draw player on the screen
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
        
        
    