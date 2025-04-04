import pygame
from rich2d.sprites.sprite import Sprite


class ScaledText(Sprite):
    DEFAULT_FONT_NAME = "monospace"
    DEFAULT_FONT_SIZE = 12
    DEFAULT_COLOUR = pygame.Color("black")

    def __init__(self, text="", colour=None,
                 font=None, font_name=None, font_size=None, font_bold=False, font_italic=False, **kwargs):
        super().__init__(**kwargs)
        if not pygame.font.get_init():
            pygame.font.init()
        if font is not None:
            self._font = font
        else:
            if font_name is None:
                font_name = ScaledText.DEFAULT_FONT_NAME
            if font_size is None:
                font_size = ScaledText.DEFAULT_FONT_SIZE
            self._font = pygame.font.SysFont(font_name, font_size, bold=font_bold, italic=font_italic)
        if colour is None:
            colour = ScaledText.DEFAULT_COLOUR
        self._text = text
        self._colour = pygame.Color(colour)
        return

    def draw(self, screen):
        if self._text == "":
            return
        font_surface = self._font.render(self._text, False, self._colour)
        font_surface = pygame.transform.scale(font_surface, (self.get_rect().width, self.get_rect().height))
        screen.blit(font_surface, self.get_rect())
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
