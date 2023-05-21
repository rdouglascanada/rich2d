import pygame
from abc import ABC, abstractmethod


class Sprite(ABC):
    def __init__(self, rect=None):
        super().__init__()
        if rect is None:
            raise RuntimeError("Sprite cannot be initialized without rect")
        self._rect = pygame.Rect(rect)
        return

    @abstractmethod
    def draw(self, screen):
        pass

    def get_rect(self):
        return self._rect
