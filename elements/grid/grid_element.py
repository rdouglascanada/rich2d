from elements.element import Element
from .grid_tiles import GridTiles


class GridElement(Element):
    def __init__(self, sprite=None, grid=None, grid_tiles=None):
        if sprite is None:
            raise RuntimeError("GridElement sprite cannot be None")
        if grid is None:
            raise RuntimeError("GridElement grid cannot be None")

        self._sprite = sprite
        self._grid = grid
        self._grid_tiles = GridTiles(grid_tiles)
        return

    def update(self):
        new_sprite_rect = self._grid.compute_rect(self._grid_tiles)
        sprite_rect = self._sprite.get_rect()
        sprite_rect.update(new_sprite_rect)
        return

    def get_grid_tiles(self):
        return self._grid_tiles


