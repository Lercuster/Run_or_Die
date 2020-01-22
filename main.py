import sys
import pygame
from global_settings import Settings
import game_functions as gf
from player import Player
from button import Button
from stats import Stats
from grid import Grid


def run_game():
    pygame.init()
    settings = Settings()
    stats = Stats(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    player = Player(settings, screen)
    grid = Grid(settings, screen, stats)
    drawing_button = Button(settings, screen, 'Drawing', (1100, 50))
    place_button = Button(settings, screen, 'Place player', (1100, 100))
    clear_button = Button(settings, screen, 'Clear wall', (1100, 150))
    pygame.display.set_caption('run or die')
    while True:
        gf.check_event(settings, screen, player, drawing_button, place_button, clear_button, stats, grid)
        gf.check_wall_collisions(player, grid)
        player.update()
        grid.update()
        gf.update_screen(settings, screen, player, drawing_button, place_button, clear_button, grid)


run_game()