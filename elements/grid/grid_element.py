from elements.element import Element


class GridElement(Element):
    def __init__(self, sprite=None, grid=None, x_index=None, y_index=None, x_tiles=1, y_tiles=1):
        if sprite is None:
            raise RuntimeError("GridElement sprite cannot be None")
        if grid is None:
            raise RuntimeError("GridElement grid cannot be None")
        if x_index is None:
            raise RuntimeError("GridElement x_index cannot be None")
        if y_index is None:
            raise RuntimeError("GridElement y_index cannot be None")

        self._sprite = sprite
        self._grid = grid
        self._x_index = x_index
        self._y_index = y_index
        self._x_tiles = x_tiles
        self._y_tiles = y_tiles
        return

    def update(self):
        new_sprite_rect = self._grid.compute_rect(x_index=self._x_index, y_index=self._y_index,
                                                  x_tiles=self._x_tiles, y_tiles=self._y_tiles)
        sprite_rect = self._sprite.get_rect()
        sprite_rect.update(new_sprite_rect)
        return

    def get_x_index(self):
        return self._x_index

    def set_x_index(self, x_index):
        self._x_index = x_index
        return

    def get_y_index(self):
        return self._y_index

    def set_y_index(self, y_index):
        self._y_index = y_index
        return

    def get_x_tiles(self):
        return self._x_tiles

    def set_x_tiles(self, x_tiles):
        self._x_tiles = x_tiles
        return

    def get_y_tiles(self):
        return self._y_tiles

    def set_y_tiles(self, y_tiles):
        self._y_tiles = y_tiles
        return
