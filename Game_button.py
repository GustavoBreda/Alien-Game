import pygame.font


class Button ():
    """ Initialize the button atributes. """

    def __init__ (self, alien_game, screen, msg):

        # Set the screen of the button
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and propreties of the button
        self.width = 200
        self.height = 50
        self.button_color = (125, 150, 255)
        self.button_text_color = (135, 206, 235)
        self.font = pygame.font.SysFont ("comicsansms", 30)

        # Build the button's rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs showed just one time
        self.prep_msg (msg)

    def prep_msg (self, msg):
        """ Turn the message in image and center it. """

        self.msg_image = self.font.render (
                                           msg, True,
                                           self.button_text_color,
                                           self.button_color
                                          )
        
        self.msg_image_rect = self.msg_image.get_rect ()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button (self):
        """ Draw the blank button and then draw the message. """

        self.screen.fill (self.button_color, self.rect)
        self.screen.blit (self.msg_image, self.msg_image_rect)