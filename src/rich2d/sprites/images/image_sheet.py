import pygame
from .image import Image


class ImageSheet:
    def __init__(self, file_name=None, image_width=None, image_height=None):
        if file_name is None:
            raise RuntimeError("ImageSheet file_name cannot be None")
        if image_width is None:
            raise RuntimeError("ImageSheet image_width cannot be None")
        if image_height is None:
            raise RuntimeError("ImageSheet image_height cannot be None")
        self._sheet = pygame.image.load(file_name)
        self._image_width = image_width
        self._image_height = image_height
        return

    def get_image_at(self, x_index=0, y_index=0, x_tiles=1, y_tiles=1):
        rect_x = x_index * self._image_width
        rect_y = y_index * self._image_height
        rect_w = x_tiles * self._image_width
        rect_h = y_tiles * self._image_height
        rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)

        surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        surface.blit(self._sheet, (0, 0), rect)
        return Image(value=surface)

    def get_all_images(self):
        images = []
        max_x_index = self._sheet.get_rect().width // self._image_width
        max_y_index = self._sheet.get_rect().height // self._image_height
        for y in range(0, max_y_index):
            for x in range(0, max_x_index):
                images.append(self.get_image_at(x_index=x, y_index=y))
        return tuple(images)
