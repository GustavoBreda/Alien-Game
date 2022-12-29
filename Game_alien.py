from pygame.sprite import Sprite
import pygame


class Alien (Sprite):
    ''' Class to represent a single alien in the fleet. '''

    def __init__ (self, alien_game, screen):
        super().__init__()

        # Set the screen of the alien
        self.screen = screen
        self.alien_game = alien_game

        # Set the alien image and get its rect
        self.image = pygame.image.load ('images/alien_modern.bmp')
        self.rect = self.image.get_rect ()

        # Start new alien near the top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.position_x = float (self.rect.x)
    
    def check_edges (self):
        """ Return true if alien is at screen's edge. """

        screen_rect = self.screen.get_rect ()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
    
    def update (self):
        """ Move the aliens. """

        self.position_x += (
                            self.alien_game.aliens_speed *
                            self.alien_game.fleet_direction
                           )
        self.rect.x = self.position_x

    def blitme (self):
        """ Draw the ship and its current location. """

        self.screen.blit (self.image, self.rect)