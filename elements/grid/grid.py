import pygame


class Grid:
    def __init__(self, grid_rect=None, rows=1, columns=1):
        if grid_rect is None:
            raise RuntimeError("Grid grid_rect cannot be None")
        self._grid_rect = pygame.Rect(grid_rect)
        self._rows = rows
        self._columns = columns
        return

    def compute_rect(self, x_index=None, y_index=None, x_tiles=1, y_tiles=1):
        if x_index is None:
            raise RuntimeError("Grid.compute_rect x_index cannot be None")
        if y_index is None:
            raise RuntimeError("Grid.compute_rect y_index cannot be None")

        tile_w = self._grid_rect.w / self._columns
        tile_h = self._grid_rect.h / self._rows
        x = self._grid_rect.x + (tile_w * x_index)
        y = self._grid_rect.y + (tile_h * y_index)
        w = x_tiles * tile_w
        h = y_tiles * tile_h
        return pygame.Rect(x, y, w, h)
