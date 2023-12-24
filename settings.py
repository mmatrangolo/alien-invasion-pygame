class Settings:

    def __init__(self):
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        self.screen_width = 5000
        self.screen_height = 3400
        self.bg_color = (230,230,230)
        self.ship_speed = 6
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 7
        self.bullet_height = 50
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 6
        self.bullet_speed = 7.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
