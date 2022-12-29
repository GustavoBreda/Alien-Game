from time import sleep
import pygame
import sys

from Game_bullet import Bullet
from Game_alien import Alien


def check_events (alien_game, screen, play_button, stats, ship, bullets, aliens):
    """ Respond the keybuttons and mouses presseds. """
    
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos ()
            check_play_button (alien_game, screen, play_button, stats, mouse_x, mouse_y, ship, bullets, aliens)
                
        elif event.type == pygame.KEYDOWN:
            check_keydown_events (event, alien_game, screen, stats, ship, bullets)
        
        elif event.type == pygame.KEYUP:
                check_keyup_events (event, ship)

def check_keydown_events (event, alien_game, screen, stats, ship, bullets):
    """ . """

    if event.key == pygame.K_RIGHT:
            ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    elif event.key == pygame.K_ESCAPE:
        sys.exit ()
    
    elif event.key == pygame.K_SPACE:
        fire_bullets (alien_game, screen, ship, bullets)

def check_keyup_events (event, ship):
    """ . """

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button (alien_game, screen, play_button, stats, mouse_x, mouse_y, ship, bullets, aliens):
    """ Start new game when the player clicks play. """
    
    button_clicked = play_button.rect.collidepoint (mouse_x, mouse_y)
    if (button_clicked) and not (stats.game_active):

        # Hide the mouse cursor
        pygame.mouse.set_visible (False)
        
        # Reset the game statistics
        stats.reset_stats ()
        stats.game_active = True

        # Empty the list of aliens and bullets
        aliens.empty ()
        bullets.empty ()

        # Restore the iniital ship properties
        ship.image = pygame.image.load ('Images/ship_classic_2.bmp')
        stats.ships_left = 2

        # Create fleets and center the ship
        create_fleets (alien_game, screen, ship, aliens)
        ship.center_ship ()
        
def fire_bullets (alien_game, screen, ship, bullets):
    """ Create bullets only if permitted. """

    if len(bullets) < alien_game.bullets_max:
        new_bullet = Bullet (alien_game, screen, ship)
        bullets.add(new_bullet)

def update_bullets (alien_game, screen, ship, bullets, aliens):
    """ Update position of bullets and get rid of old bullets. """

    # Update bullets's positions
    bullets.update ()

    # Get rid of disappeard bullets
    for bullet in bullets.copy ():
        if bullet.rect.bottom <= 0:
            bullets.remove (bullet)
    
    check_bullet_collision (alien_game, screen, ship, bullets, aliens)
    
def check_bullet_collision (alien_game, screen, ship, bullets, aliens):
    """ Respond to bullet-allien collision. """

    collisions = pygame.sprite.groupcollide (bullets, aliens, True, True)

    if len (aliens) == 0:
        bullets.empty()
        create_fleets (alien_game, screen, ship, aliens)

def get_number_aliens (alien_game, alien_width):
    """ Determine the number of aliens permitted in a row. """

    available_space_x = alien_game.screen_width - 50
    number_aliens_x = available_space_x // int (1.3 * alien_width)

    return number_aliens_x

def get_number_rows (alien_game, ship_height, alien_height):
    """ Determine the number of rows permitted in the screen. """

    available_space_y = (alien_game.screen_height - (6 * alien_height) - ship_height)
    number_rows = int (available_space_y // (1.3 * alien_height))

    return number_rows

def create_alien (alien_game, screen, row_number, alien_width, aliens, alien_number):
    """ Create an alien and place it in a row. """

    alien = Alien (alien_game, screen)
    alien.position_x = 50 + (1.3 * alien_width * alien_number)
    alien.rect.x = alien.position_x
    alien.rect.y = 30 + (1.3 * alien.rect.height * row_number)
    aliens.add (alien)

def create_fleets (alien_game, screen, ship, aliens):
    """ Create a full fleet of aliens. """

    # The space between two aliens is one alien width
    alien = Alien (alien_game, screen)
    number_aliens_x = get_number_aliens (alien_game, alien.rect.width)
    number_rows = get_number_rows (alien_game, ship.rect.height, alien.rect.height)

    for row in range (number_rows):
        for alien_number in range (number_aliens_x):
            create_alien (alien_game, screen, row, alien.rect.width, aliens, alien_number)

def check_fleet_edges (alien_game, aliens):
    """ Respond appropriately if an alien reach the edges. """

    for alien in aliens.sprites ():
        # Why sprites make the aliens takes Alien methord???
        if alien.check_edges ():
            change_fleet_direction (alien_game, aliens)
            break

def change_fleet_direction (alien_game, aliens):
    """ Drop the entire fleet and change the fleet's direction. """
    
    for alien in aliens.sprites ():
        alien.rect.y += alien_game.fleet_drop_speed
    
    alien_game.fleet_direction *= -1

def ship_hit (alien_game, screen, stats, ship, bullets, aliens):
    """ Respond to hits. """

    if stats.ships_left > 0:

        # Start the number of ships losted
        stats.ships_left -= 1

        # Empty the list of bullets and aliens
        bullets.empty()
        aliens.empty()

        # New fleet
        create_fleets (alien_game, screen, ship, aliens)
        ship.center_ship()

        if stats.ships_left == 1:
            ship.image = pygame.image.load ('Images/ship_modern.bmp')
        if stats.ships_left == 0:
            ship.image = pygame.image.load ('Images/ship_future.bmp')
            
        sleep (0.2)
    
    else:
        ship.center_ship()
        bullets.empty()
        aliens.empty()
        stats.game_active = False
        pygame.mouse.set_visible (True)

def check_aliens_bottom (alien_game, screen, stats, ship, bullets, aliens):
    """ Check if any aliens have reached the bottom of the screen. """

    screen_rect = screen.get_rect ()
    for alien in aliens.sprites ():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit (alien_game, screen, stats, ship, bullets, aliens)
            break

def update_aliens (alien_game, screen, stats, ship, bullets, aliens):
    """ . """

    check_fleet_edges (alien_game, aliens)
    aliens.update ()

    # Look for alien-ship collision
    if pygame.sprite.spritecollideany (ship, aliens):
        ship_hit (alien_game, screen, stats, ship, bullets, aliens)
    
    # Look for bottoms's aliens
    check_aliens_bottom (alien_game, screen, stats, ship, bullets, aliens)

def update_screen (alien_game, screen, play_button, stats, ship, bullets, aliens):
    """ Updates images on the screen. """

    # Redraw the screen on every loop
    screen.fill (alien_game.screen_bg)
    
    # ship.image.fill (alien_game.screen_bg)
    aliens.draw (screen)
    ship.blitme ()

    # Redraw all bullets
    for bullet in bullets.sprites ():
        bullet.draw_bullet ()
    
    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button ()

    # flip() make the last drawn screen visible
    pygame.display.flip()