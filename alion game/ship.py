# this module will control most of the players movemens inside the game
import pygame
class Ship:
    """Class to control the player ship movements"""
    def __init__(self, ai_game):
        """initilize the player and set the starting position"""
        self.screen = ai_game.screen

        # this is to control the speed of the ship in the game
        self.settings = ai_game.settings


        # movement Flag
        self.moving_right = False
        self.moving_left = False

        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship images and give the rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start the every ship at the midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store the float values for the ship to move faster than 1 pixel at one cycle
        self.x = float(self.rect.x)

    def update(self):
        # set the condition to prevent the ship from moving out of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):

        """Draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)
