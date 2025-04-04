import pygame
from abc import ABC, abstractmethod


class Sprite(ABC):
    def __init__(self, rect=None, visible=True):
        super().__init__()
        if rect is None:
            raise RuntimeError("Sprite cannot be initialized without rect")
        self._rect = pygame.Rect(rect)
        self._visible = visible
        return

    @abstractmethod
    def draw(self, screen):
        pass

    def get_rect(self):
        return self._rect

    def draw_if_visible(self, screen):
        if self._visible:
            self.draw(screen)
        return

    def is_visible(self):
        return self._visible

    def set_visible(self, visible):
        self._visible = visible
        return


