class Settings:
    def __init__(self):
        self.window_width = 800
        self.window_height = 500
        self.bg_color = (230,230,230)
        #player properties
        self.player_lives_left = 3
        
        
        #Projectile attributes
        self.projectile_color = (250,0,0)
        self.projectile_width = 5
        self.projectile_hight = 15
        
        
        #enemy attributes
        
        self.enemies_number = 4
        
        #collectible_attribute
        self.collectible_num =1
        
        # how quickly the game speeds up
        self.speed_up_factor = 1.1
        
        #initialize dynamic settings attributes
        self.initialize_dynamic_attr()
        
    def initialize_dynamic_attr(self):
        self.player_speed_factor = 1
        self.enemy_speed_factor = 0.05
        self.projectile_speed_factor = 2
        #scoring
        self.enemy_hit_points = 20
    
    def increase_speed(self):
        self.player_speed_factor *= self.speed_up_factor
        self.projectile_speed_factor *= self.speed_up_factor
        self.enemy_speed_factor *= self.speed_up_factor