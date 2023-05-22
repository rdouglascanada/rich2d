import pygame
from .sprite import Sprite


class Rectangle(Sprite):
    DEFAULT_COLOUR = pygame.Color("black")

    def __init__(self, rect=None, colour=None):
        super().__init__(rect=rect)
        if colour is None:
            colour = Rectangle.DEFAULT_COLOUR
        self._colour = pygame.Color(colour)
        return

    def draw(self, screen):
        pygame.draw.rect(screen, self._colour, self._rect)
        return

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        self._colour = pygame.Color(colour)
        return
