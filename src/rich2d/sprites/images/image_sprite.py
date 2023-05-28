import pygame
from rich2d.sprites import Sprite


class ImageSprite(Sprite):
    def __init__(self, image=None, **kwargs):
        if image is None:
            raise RuntimeError("ImageSprite image cannot be None")
        super().__init__(**kwargs)
        self._image = image
        return

    def draw(self, screen):
        image_surface = self._image.get_value()
        image_surface = pygame.transform.scale(image_surface, (self.get_rect().width, self.get_rect().height))
        screen.blit(image_surface, self.get_rect())
        return
