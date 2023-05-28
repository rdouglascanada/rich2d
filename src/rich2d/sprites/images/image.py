import pygame


class Image:
    def __init__(self, file_name=None):
        if file_name is None:
            raise RuntimeError("Image file_name cannot be None")
        self._image = pygame.image.load(file_name)
        return

    def get_value(self):
        return self._image
