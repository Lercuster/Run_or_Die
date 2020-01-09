import sys
import pygame
from global_settings import Settings
import game_functions as gf
from player import Player
from button import Button


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    player = Player(settings, screen)
    drawing_button = Button(screen, 'Drawing', (1100, 50))
    play_button = Button(screen, 'Play', (1100, 100))
    pygame.display.set_caption('run or die')

    while True:
        gf.check_event(player, drawing_button, play_button)
        player.update()
        gf.update_screen(settings, screen, player, drawing_button, play_button)


run_game()