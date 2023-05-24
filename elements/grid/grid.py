import pygame


class Grid:
    def __init__(self, rect=None, rows=1, columns=1):
        if rect is None:
            raise RuntimeError("Grid grid_rect cannot be None")
        self._rect = pygame.Rect(rect)
        self._rows = rows
        self._columns = columns
        return

    def compute_rect(self, grid_tiles):
        tile_w = self._rect.w / self._columns
        tile_h = self._rect.h / self._rows
        x = self._rect.x + (tile_w * grid_tiles.get_x_index())
        y = self._rect.y + (tile_h * grid_tiles.get_y_index())
        w = grid_tiles.get_x_tiles() * tile_w
        h = grid_tiles.get_y_tiles() * tile_h
        return pygame.Rect(x, y, w, h)
