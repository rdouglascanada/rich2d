import pygame
from rich2d.sprites.sprite import Sprite


class Circle(Sprite):
    DEFAULT_COLOUR = pygame.Color("black")

    def __init__(self, rect=None, colour=None):
        super().__init__(rect=rect)
        if colour is None:
            colour = Circle.DEFAULT_COLOUR
        self._colour = pygame.Color(colour)
        return

    def draw(self, screen):
        pygame.draw.ellipse(screen, self._colour, self._rect)
        return

    def get_colour(self):
        return self._colour
