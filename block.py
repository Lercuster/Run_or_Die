import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    """ a block of wall """
    def __init__(self, settings, screen, posx, posy):
        super(Block, self).__init__()
        self.color = settings.block_color
        self.screen = screen
        self.centerx = posx
        self.centery = posy
        self.width = settings.grid_block_size

    def draw_block(self):
        """ draw a rect block """
        pygame.draw.rect(self.screen, self.color, (self.centerx, self.centery, self.width, self.width))

