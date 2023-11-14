# we use this class to import or set all the settings in the game
class Settings:
    """a class to store all the settings for the alien invsion"""
    def __init__(self):
        """initilize the game settings"""
        self.bg_color = (230,230,230)
        self.screen_width= 1200
        self.screen_height = 750
        # ship speed
        self.ship_speed = 1.5
        # these settings we are going to use with to shoot bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        # limiting the bullets
        self.bullet_allowed = 3
