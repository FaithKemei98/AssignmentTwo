class Settings:
    def __init__(self):
        self.window_width = 800
        self.window_height = 500
        self.bg_color = (230,230,230)
        #player properties
        self.player_lives_left = 3
        self.move_speed_factor = 1
        
        #Projectile attributes
        self.projectile_color = (250,0,0)
        self.projectile_width = 5
        self.projectile_hight = 15
        self.projectile_speed_factor = 2
        
        #enemy attributes
        self.enemy_speed_factor = 0.05
        self.enemies_number = 4
        
        #collectible_attribute
        self.collectible_num =1
        