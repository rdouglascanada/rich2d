import pygame


class Image:
    def __init__(self, value=None):
        if value is None:
            raise RuntimeError("Image value cannot be None")
        self._image = value
        return

    def get_value(self):
        return self._image

    @staticmethod
    def load_from_file(file_name=None):
        if file_name is None:
            raise RuntimeError("Image.load_from_file file_name cannot be None")
        image_value = pygame.image.load(file_name)
        return Image(value=image_value)
