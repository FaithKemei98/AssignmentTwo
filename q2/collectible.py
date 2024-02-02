import pygame
from pygame.sprite import Sprite
import random

class Collectible(Sprite):
    def __init__(self, screen, settings):
        super(Collectible, self).__init__()
        self.screen = screen
        self.settings = settings
        
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()
        
        
        #random position of a collectible on the screen.
        self.width = random.randint(0,800)
        self.height = random.randint(0,400)
        
        self.rect.x = self.width
        self.rect.y = self.height
        
    #draw collectible on the screen
    def blit_me(self):
        self.screen.blit(self.image, self.rect)