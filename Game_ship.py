import pygame


class Ship ():
    """ Class to initialize the ship ans set its start position """

    def __init__ (self, alien_game, screen):

        # Set the screen of the ship
        self.screen = screen
        self.alien_game = alien_game

        # Load the ship image and get its rectangles
        self.image = pygame.image.load ('Images/ship_classic_2.bmp')
        self.image.set_colorkey ((230, 230, 230))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        # Start the ship at the bottom center of the rectangle screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float values for the ship's center
        self.center = float (self.rect.centerx)

        # Check movement to right or left
        self.moving_right = False
        self.moving_left = False

    def update (self):
        """ Update the ships position. """

        if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.alien_game.ships_speed
        if self.moving_left and self.rect.left > 0:
                self.center -= self.alien_game.ships_speed

        self.rect.centerx = self.center

    def center_ship (self):
        """ Center the ship on the screen. """
        
        self.center = self.screen_rect.centerx

    def blitme (self):
        """ Draw the ship and its current location. """

        self.screen.blit (self.image, self.rect)