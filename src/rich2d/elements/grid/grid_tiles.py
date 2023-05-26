class GridTiles:
    def __init__(self, values):
        if (type(values) is list) or (type(values) is tuple):
            x_index = values[0]
            y_index = values[1]
            x_tiles = values[2]
            y_tiles = values[3]
        else:
            x_index = values.get_x_index()
            y_index = values.get_y_index(),
            x_tiles = values.get_x_tiles()
            y_tiles = values.get_y_tiles()

        if x_index is None:
            raise RuntimeError("GridTiles x_index cannot be None")
        if y_index is None:
            raise RuntimeError("GridTiles y_index cannot be None")

        self._x_index = x_index
        self._y_index = y_index
        self._x_tiles = x_tiles
        self._y_tiles = y_tiles
        return

    def collides_with(self, grid_tiles):
        x_collides = (self._x_index <= grid_tiles.get_x_index() < self._x_index + self._x_tiles) or \
                     (grid_tiles.get_x_index() <= self._x_index < grid_tiles.get_x_index() + grid_tiles.get_x_tiles())
        y_collides = (self._y_index <= grid_tiles.get_y_index() < self._y_index + self._y_tiles) or \
                     (grid_tiles.get_y_index() <= self._y_index < grid_tiles.get_y_index() + grid_tiles.get_y_tiles())
        return x_collides and y_collides

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
