import pygame
from pygame.sprite import Sprite


class Bullet (Sprite):
    " Class to manage the bullets fired from the ship "

    def __init__ (self, alien_game, screen, ship):
        super().__init__()

        # Set the screen of the bullet
        self.screen = screen

        # Set the bullets's instances about its postions
        self.rect = pygame.Rect (
                                 0, 0, 
                                 alien_game.bullet_width,
                                 alien_game.bullet_height
                                )
        
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.rect.top -= 10
        self.position_y = float (self.rect.y)

        # Set bullets's characteristcs
        self.color = alien_game.bullet_color
        self.bullets_speed = alien_game.bullets_speed
    
    def update (self):
        " Update the bullets position to up. "

        self.position_y -= self.bullets_speed
        self.rect.y = self.position_y 
    
    def draw_bullet (self):
        " Draw the bullets to the screen. "

        pygame.draw.rect (self.screen, self.color, self.rect)