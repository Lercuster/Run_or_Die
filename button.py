import pygame.font


class Button():
    def __init__(self, settings, screen, msg, position):
        self.screen = screen
        self.settings = settings
        self.msg = msg
        self.screen_rect = screen.get_rect()
        self.width = 200
        self.height = 25
        self.button_color_unclicked = (255, 0, 0)
        self.button_color_clicked = (0, 255, 0)
        self.button_color = self.button_color_unclicked
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = position
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def change_color(self):
        if self.button_color == self.button_color_unclicked:
            self.button_color = self.button_color_clicked
        else:
            self.button_color = self.button_color_unclicked
        self.prep_msg(self.msg)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
