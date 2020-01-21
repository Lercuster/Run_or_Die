import sys
import pygame
from global_settings import Settings
import game_functions as gf
from player import Player
from button import Button
from block import Block
from stats import Stats
from pygame.sprite import Group
from grid import Grid


def run_game():
    pygame.init()
    settings = Settings()
    stats = Stats(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    player = Player(settings, screen)
    drawing_button = Button(screen, 'Drawing', (1100, 50))
    play_button = Button(screen, 'Play', (1100, 100))
    blocks = Group()
    grid = Grid(settings, screen, blocks, stats)
    pygame.display.set_caption('run or die')
    while True:
        gf.check_event(settings, screen, player, drawing_button, play_button, stats, blocks, grid)
        gf.check_wall_collisions(player, grid)
        player.update()
        grid.update()
        gf.update_screen(settings, screen, player, drawing_button, play_button, blocks, grid)


run_game()