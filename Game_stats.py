class Game_Stats ():
    """ Track the statistics for the game. """

    def __init__ (self, alien_game):
        """Initialize statistics."""

        self.alien_game = alien_game
        self.reset_stats ()

        # Start game in an inactive state
        self.game_active = False

    def reset_stats (self):
        """Initialize statistics that can change during the game."""

        self.ships_left = self.alien_game.ship_limit