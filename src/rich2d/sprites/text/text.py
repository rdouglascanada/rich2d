import pygame
from enum import Enum
from rich2d.sprites.sprite import Sprite


class Text(Sprite):
    DEFAULT_FONT_NAME = "monospace"
    DEFAULT_FONT_SIZE = 12
    DEFAULT_COLOUR = pygame.Color("black")

    class HorizontalAlignment(Enum):
        LEFT = 1
        CENTRE = 2
        RIGHT = 3

    class VerticalAlignment(Enum):
        TOP = 1
        MIDDLE = 2
        BOTTOM = 3

    def __init__(self, rect=None, text="", colour=None,
                 font=None, font_name=None, font_size=None, font_bold=False, font_italic=False,
                 horizontal_alignment=HorizontalAlignment.CENTRE, vertical_alignment=VerticalAlignment.MIDDLE):
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
        self._horizontal_alignment = horizontal_alignment
        self._vertical_alignment = vertical_alignment
        return

    def draw(self, screen):
        text_width, text_height = self._font.size(self._text)
        font_surface = self._font.render(self._text, False, self._colour)

        if self._horizontal_alignment == Text.HorizontalAlignment.LEFT:
            x_displacement = 0
        elif self._horizontal_alignment == Text.HorizontalAlignment.RIGHT:
            x_displacement = self.get_rect().w - text_width
        else:
            x_displacement = (self.get_rect().w - text_width) / 2

        if self._vertical_alignment == Text.VerticalAlignment.TOP:
            y_displacement = 0
        elif self._vertical_alignment == Text.VerticalAlignment.BOTTOM:
            y_displacement = self.get_rect().h - text_height
        else:
            y_displacement = (self.get_rect().h - text_height) / 2

        text_x = self.get_rect().x + x_displacement
        text_y = self.get_rect().y + y_displacement
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
