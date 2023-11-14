import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """here we control the alien behaviou in our game"""
    def __init__(self, ai_game):
        """initilize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and its rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start every alien on the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alion exact horizontal position
        self.x = float(self.rect.x)
