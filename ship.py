import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, sg):
        """Initialize the ship and set its starting position"""
        self.screen = sg.screen
        self.settings = sg.settings
        self.screen_rect = sg.screen.get_rect()
      

        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images\ship.bmp')
        new_width = 50
        new_height = 50
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()        

        # start each new ship at the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)