import pygame


class Rectangle:
    DEFAULT_RECT = pygame.Rect((0, 0), (0, 0))
    DEFAULT_COLOUR = pygame.Color("black")

    def __init__(self, rect=None, colour=None):
        if rect is None:
            rect = Rectangle.DEFAULT_RECT
        if colour is None:
            colour = Rectangle.DEFAULT_COLOUR
        self._rect = pygame.Rect(rect)
        self._colour = pygame.Color(colour)
        return

    def draw(self, screen):
        pygame.draw.rect(screen, self._colour, self._rect)
        return

    def get_rect(self):
        return self._rect

    def get_colour(self):
        return self._colour
