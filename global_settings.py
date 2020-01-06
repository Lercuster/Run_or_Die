class Settings():
    """
    class where all settings are stored.
    """
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 600
        self.background_color = (0, 0, 0)
        self.player_speed = 0.7
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        pass
