# in this project we are going to build the alien game by using the pygame library so lets start
# firstly we import the library named pygame this is especially use to construct game in python
import sys
from settings import Settings
from ship import Ship
import pygame
from  bullets import Bullet
from alien import Alien


class AlienInvasion:
    """this class is going to control all over the classs and behaviours of the class """

    def __init__(self):
        """overall we use this method to setup the game envirnment and resources"""
        # we use init method to use the all over the dependencies or we can say settings that pygame use to build the
        # game

        # create object settings in settings class
        pygame.init()
        self.settings = Settings()


        # we use values in settings class to initilize in this set mode
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('alien invasion is the best game')

        # here we define the pygame display to the full screen size we define the initial stage to 0 0
        # because we dont know the device screen size
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)

        # storing the bullets in group
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """make an alien"""
        alien = Alien(self)
        self.aliens.add(alien)







    def run_game(self):
        """we use this to start a loop that control overall the game"""
        while True:

            # now we are going to learn something new abut helping methods that are start with _ underscore
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # delete the unnecessory bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()


    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                   self._check_keyup(event)

    # use these helper methods to check the keydown and keyup events
    def _check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """create a new bullet and add it to the bullts group"""
        if len(self.bullets)< self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_screen(self):
        """this is use to update the screen while game is playing"""
        # watch the keyboard and mouse events
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
