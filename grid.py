import pygame
from block import Block


class Grid():

    def __init__(self, settings, screen, blocks, stats):
        self.settings = settings
        self.screen = screen
        self.mouse_press = stats.drawing_mode[0]
        self.body = blocks
        self.mouse_x = 0
        self.mouse_y = 0

    def get_correct_block_position(self, posx, posy):
        """ calc a correct coords to fill a grid block """
        posx_true = ((posx - self.settings.grid_block_size) // self.settings.grid_block_size + 1) * self.settings.grid_block_size
        posy_true = ((posy - self.settings.grid_block_size) // self.settings.grid_block_size + 1) * self.settings.grid_block_size
        return posx_true, posy_true

    def update(self):
        if self.mouse_press:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            if self.mouse_x >= self.settings.grid_left and self.mouse_x <= self.settings.grid_right:
                if self.mouse_y >= self.settings.grid_up and self.mouse_y <= self.settings.grid_bottom:
                    posx_true, posy_true = self.get_correct_block_position(self.mouse_x, self.mouse_y)
                    block = Block(self.settings, self.screen, posx_true, posy_true)
                    self.body.add(block)

    def draw_all_blocks(self):
        for block in self.body:
            block.draw_block()