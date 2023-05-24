import pygame
from .sprite import Sprite


class Polygon(Sprite):
    DEFAULT_COLOUR = pygame.Color("black")

    def __init__(self, rect=None, colour=None, points=None):
        if points is None:
            raise RuntimeError("Polygon points cannot be None")
        if len(points) < 3:
            raise RuntimeError("Polygon points must consist of at least 3 values")
        super().__init__(rect=rect)
        if colour is None:
            colour = Polygon.DEFAULT_COLOUR
        self._colour = colour
        self._points = points
        return

    def draw(self, screen):
        rect = self.get_rect()
        adjusted_points = tuple((rect.x + (p[0] * rect.w), rect.y + (p[1] * rect.h)) for p in self._points)
        pygame.draw.polygon(screen, self._colour, adjusted_points, width=0)
        return
