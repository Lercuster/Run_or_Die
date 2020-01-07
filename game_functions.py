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


def check_drawing_button(drawing_button, mouse_x, mouse_y):
    """ """
    butt_clicked = drawing_button.rect.collidepoint(mouse_x, mouse_y)
    if butt_clicked:
        print("drawing button is clicked")


def check_play_button(play_button, mouse_x, mouse_y):
    butt_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if butt_clicked:
        print('play button is clicked')


def check_event(player, drawing_button, play_button):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_drawing_button(drawing_button, mouse_x, mouse_y)
            check_play_button(play_button, mouse_x, mouse_y)


def update_screen(settings, screen, player, drawing_button, play_button):
    """
    Updating screen.
    """
    screen.fill(settings.background_color)
    player.blitme()
    drawing_button.draw_button()
    play_button.draw_button()
    pygame.display.flip()


if __name__ == '__main__':
    print('kvsugvd')