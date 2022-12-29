class Settings ():
    """ Class to initialize the game settings. """
    
    def __init__ (self):

        # Screen settings
        self.screen_width = 1360
        self.screen_height = 768
        self.screen_bg = (135, 206, 235)

        # Ship settings
        self.ships_speed = 1.3
        self.ship_limit = 2

        # Alien settings
        self.aliens_speed = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        # Bullet settings
        self.bullets_max = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullets_speed = 3
        self.bullet_color = 40, 245, 48