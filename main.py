import sys
import pygame
from global_settings import Settings
import game_functions as gf
from player import Player


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    player = Player(settings, screen)
    pygame.display.set_caption('run or die')

    while True:
        gf.check_event(player)
        player.update()
        gf.update_screen(settings, screen, player)


run_game()
