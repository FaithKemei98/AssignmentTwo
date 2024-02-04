import pygame
from pygame.sprite import  Sprite
import random
class Enemy(Sprite):
    def __init__(self, settings, screen):
        super(Enemy, self).__init__()
        self.settings = settings
        self.screen = screen
        
        #Enemies image
        self.image = pygame.image.load('images/enemy.jpg')
        self.rect = self.image.get_rect()
        
        #create a random points from which the enemy will start from
        
        rand_width = random.randint(0, 750)
        rand_height = random.randint(0,100)
        
        
        
        #start each image at a random position
        self.rect.x = rand_width
        self.rect.y = rand_height
        
        #get the y position of the enemy on the screen
        self.y = float(self.rect.y)
        
    def update(self):
        self.y += self.settings.enemy_speed_factor
        self.rect.y = self.y
    
    #drawing the alien on the screen.
    def blitMe(self):
        self.screen.blit(self.image, self.rect)