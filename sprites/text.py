import pygame
from .sprite import Sprite


class Text(Sprite):
    DEFAULT_FONT_NAME = "monospace"
    DEFAULT_FONT_SIZE = 12
    DEFAULT_COLOUR = pygame.Color("black")

    def __init__(self, rect=None, text="", colour=None,
                 font=None, font_name=None, font_size=None, font_bold=False, font_italic=False):
        super().__init__(rect=rect)
        if not pygame.font.get_init():
            pygame.font.init()
        if font is not None:
            self._font = font
        else:
            if font_name is None:
                font_name = Text.DEFAULT_FONT_NAME
            if font_size is None:
                font_size = Text.DEFAULT_FONT_SIZE
            self._font = pygame.font.SysFont(font_name, font_size, bold=font_bold, italic=font_italic)
        if colour is None:
            colour = Text.DEFAULT_COLOUR
        self._text = text
        self._colour = pygame.Color(colour)
        return

    def draw(self, screen):
        text_width, text_height = self._font.size(self._text)
        font_surface = self._font.render(self._text, False, self._colour)
        text_x = self.get_rect().x + (self.get_rect().w - text_width) / 2
        text_y = self.get_rect().y + (self.get_rect().h - text_height) / 2
        screen.blit(font_surface, (text_x, text_y, text_width, text_height))
        return

    def get_font(self):
        return self._font

    def set_font(self, font):
        self._font = font
        return

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        return

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        self._colour = colour
        return
