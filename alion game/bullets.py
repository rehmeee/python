# we are going to handle all tasks of bullets
import  pygame
from  pygame.sprite import Sprite
class Bullet(Sprite):
    """intinially this class control the behaviour of the bullets"""
    def __init__(self,ai_game):
        """create bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create the bullet react at (0,0 )and then set to the correct position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """move the bullets up the screen"""
        self.y -=self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullets to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
