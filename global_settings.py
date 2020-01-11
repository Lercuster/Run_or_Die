class Settings():
    """
    class where all settings are stored.
    """
    def __init__(self):

        # screen settings #
        self.screen_width = 1250
        self.screen_height = 600
        self.game_field_width = 950
        self.grid_block_size = 25
        self.grid_left = self.grid_block_size
        self.grid_up = self.grid_block_size
        self.grid_right = self.game_field_width - self.grid_block_size
        self.grid_bottom = self.screen_height - self.grid_block_size
        self.background_color = (0, 0, 0)

        # player settings #
        self.grid_color = (50, 50, 50)
        self.player_color = (255, 0, 0)
        self.player_radius = 10
        self.player_speed = 0.1
        self.initialize_dynamic_settings()

        # block settings #
        self.block_color = (200, 200, 200)


    def initialize_dynamic_settings(self):
        pass
