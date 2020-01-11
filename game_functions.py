import pygame
import sys
from global_settings import Settings
from time import sleep
from random import randint
from block import Block


def draw_grid(settings, screen):
    block_size = settings.grid_block_size
    rows = settings.game_field_width // block_size
    x = block_size
    y = block_size
    pygame.draw.line(screen, settings.grid_color, (settings.game_field_width, 0),
                     (settings.game_field_width, settings.screen_height))
    pygame.draw.line(screen, settings.grid_color, (block_size, block_size), (block_size, settings.screen_height - block_size))
    pygame.draw.line(screen, settings.grid_color, (block_size, block_size), (settings.game_field_width - block_size, block_size))
    for i in range(rows-2):
        x += block_size
        y += block_size
        pygame.draw.line(screen, settings.grid_color, (x, block_size), (x, settings.screen_height-block_size))
        pygame.draw.line(screen, settings.grid_color, (block_size, y), (settings.game_field_width-block_size, y))


def check_keydown_event(event, player):
    """
    check button pressed events. if button is pushed, flag a player to move
    """
    if event.key == pygame.K_RIGHT:
        if player.moving:
            player.steering_vector = player.get_orto_vector('r')
    if event.key == pygame.K_LEFT:
        if player.moving:
            player.steering_vector = player.get_orto_vector('l')
    if event.key == pygame.K_UP:
        player.moving = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, player):
    """
    analog to keydown, but with keyup events
    """
    if event.key == pygame.K_UP:
        player.moving = False


def check_drawing_button(drawing_button, mouse_x, mouse_y):
    """ check is drawing button is clicked """
    butt_clicked = drawing_button.rect.collidepoint(mouse_x, mouse_y)
    if butt_clicked:
        print("drawing button is clicked")


def check_play_button(play_button, mouse_x, mouse_y):
    """ check is play button is clicked """
    butt_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if butt_clicked:
        print('play button is clicked')


def check_event(settings, screen, player, drawing_button, play_button, stats, blocks):
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
            stats.drawing_mode = pygame.mouse.get_pressed()
            if stats.drawing_mode[0]:
                create_grid_block(settings, screen, mouse_x, mouse_y, blocks)


def get_correct_block_position(settings, posx, posy):
    """ calc a correct coords to fill a grid block """
    posx_true = ((posx - settings.grid_block_size) // settings.grid_block_size + 1) * settings.grid_block_size
    posy_true = ((posy - settings.grid_block_size) // settings.grid_block_size + 1) * settings.grid_block_size
    return posx_true, posy_true


def create_grid_block(settings, screen, posx, posy, blocks):
    """ create a wall block """
    if posx >= settings.grid_left and posx <= settings.grid_right:
        if posy >= settings.grid_up and posy <= settings.grid_bottom:
            posx_true, posy_true = get_correct_block_position(settings, posx, posy)
            block = Block(settings, screen, posx_true, posy_true)
            blocks.add(block)


def update_screen(settings, screen, player, drawing_button, play_button, blocks):
    """
    Updating screen.
    """
    screen.fill(settings.background_color)
    draw_grid(settings, screen)
    player.blitme()
    drawing_button.draw_button()
    play_button.draw_button()
    for block in blocks:
        block.draw_block()
    pygame.display.flip()


if __name__ == '__main__':
    print('kvsugvd')
