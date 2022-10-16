class Settings:
    """ A class t store all settings for Alien Invasion."""

    def __init__(self):
        """ Initialize teh game's settings."""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230,230,230)

        # ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represent right: -1 represent left.
        self.fleet_direction = 1



