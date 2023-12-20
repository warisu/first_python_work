class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, sg):
        """Initialize statistics."""
        self.settings = sg.settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit