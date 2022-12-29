from pygame.sprite import Group
import pygame

from Game_functions import check_events
from Game_functions import create_fleets
from Game_functions import update_screen
from Game_functions import update_aliens
from Game_functions import update_bullets

from Game_settings import Settings
from Game_stats import Game_Stats
from Game_button import Button
from Game_ship import Ship


def run_game ():
    """ Call the methods and run the game. """

    pygame.init ()
    alien_game = Settings ()
    screen = pygame.display.set_mode (
                                        (alien_game.screen_width, alien_game.screen_height)
                                     )

    pygame.display.set_caption ("Alien Invasion")

    # Make the play button
    play_button = Button (alien_game, screen, "PLAY")
    stats = Game_Stats (alien_game)

    # What Group () does?
    ship = Ship (alien_game, screen)
    bullets = Group ()
    aliens = Group ()

    # Creating a fleet of aliens
    create_fleets (alien_game, screen, ship, aliens)

    while True:

        check_events (alien_game, screen, play_button, stats, ship, bullets, aliens)
        
        if stats.game_active:
            Ship.update (ship)
            update_bullets (alien_game, screen, ship, bullets, aliens)
            update_aliens (alien_game, screen, stats, ship, bullets, aliens)
        
        update_screen (alien_game, screen, play_button, stats, ship, bullets, aliens)

            
run_game ()