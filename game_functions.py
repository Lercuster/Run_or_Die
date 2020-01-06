import pygame
import sys
from global_settings import Settings
from time import sleep
from random import randint


def check_keydown_event(event, player):
    """
    check button pressed events. if button is pushed, flag a player to move
    """
    if event.key == pygame.K_RIGHT:
        player.move_right = True
    if event.key == pygame.K_LEFT:
        player.move_left = True
    if event.key == pygame.K_UP:
        player.move_up = True
    if event.key == pygame.K_DOWN:
        player.move_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, player):
    """
    analog to keydown, but with keyup events
    """
    if event.key == pygame.K_RIGHT:
        player.move_right = False
    if event.key == pygame.K_LEFT:
        player.move_left = False
    if event.key == pygame.K_UP:
        player.move_up = False
    if event.key == pygame.K_DOWN:
        player.move_down = False


def check_event(player):
    """
    Function which is calling check keydown/keyup.
    Checks events in general and deal with them.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, player)


def update_screen(settings, screen, player):
    """
    Updating screen.
    """
    screen.fill(settings.background_color)
    player.blitme()
    pygame.display.flip()


if __name__ == '__main__':
    print('kvsugvd')