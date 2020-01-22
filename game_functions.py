import pygame
import sys


def draw_grid(settings, screen):
    """ drawing grid """
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


def check_drawing_button(settings, drawing_button, mouse_x, mouse_y, grid):
    """ check is drawing button is clicked """
    butt_clicked = drawing_button.rect.collidepoint(mouse_x, mouse_y)
    if butt_clicked:
        if not settings.drawing_mode:
            settings.drawing_mode = True
            drawing_button.change_color()
        else:
            settings.drawing_mode = False
            drawing_button.change_color()
    if settings.drawing_mode:
        grid.mouse_press = pygame.mouse.get_pressed()[0]
        grid.mouse_x = mouse_x
        grid.mouse_y = mouse_y


def check_place_button(settings, place_button, mouse_x, mouse_y, player):
    """ check is play button is clicked """
    butt_clicked = place_button.rect.collidepoint(mouse_x, mouse_y)
    coords_in_grid = player.bound_right > mouse_x > player.bound_left and \
                        player.bound_bottom > mouse_y > player.bound_up
    print(coords_in_grid)
    if butt_clicked:
        if not settings.placing_mode:
            settings.placing_mode = True
            place_button.change_color()
        else:
            settings.placing_mode = False
            place_button.change_color()
    else:
        if settings.placing_mode and coords_in_grid:
            settings.placing_mode = False
            place_button.change_color()

def check_clear_button(settings, clear_button, mouse_x, mouse_y, grid):
    """ check is clear button is clicked """
    butt_clicked = clear_button.rect.collidepoint(mouse_x, mouse_y)
    if butt_clicked:
        grid.clear()


def check_event(settings, screen, player, drawing_button, place_button, clear_button, stats, grid):
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
            check_drawing_button(settings, drawing_button, mouse_x, mouse_y, grid)
            check_place_button(settings, place_button, mouse_x, mouse_y, player)
            check_clear_button(settings, clear_button, mouse_x, mouse_y, grid)
        elif event.type == pygame.MOUSEBUTTONUP:
            grid.mouse_press = pygame.mouse.get_pressed()[0]


def check_wall_collisions(player, grid):
    """ check collisions between player and wall blocks """
    collisions = pygame.sprite.spritecollideany(player, grid.body)
    if collisions:
        player.reset_to_initial_pos()


def update_screen(settings, screen, player, drawing_button, play_button, clear_button, grid):
    """
    Updating screen.
    """
    screen.fill(settings.background_color)
    draw_grid(settings, screen)
    drawing_button.draw_button()
    grid.draw_all_blocks()
    play_button.draw_button()
    clear_button.draw_button()
    if settings.placing_mode:
        player.start_pos_center = pygame.mouse.get_pos()[0]
        player.start_pos_bottom = pygame.mouse.get_pos()[1]
        player.reset_to_initial_pos()
    player.blitme()
    pygame.display.update()
