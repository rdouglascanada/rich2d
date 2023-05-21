from pygame import Color


class GameConfig:
    DEFAULT_BACKGROUND_COLOUR = Color("black")
    DEFAULT_WINDOW_WIDTH = 800
    DEFAULT_WINDOW_HEIGHT = 600

    def __init__(self, background_colour=None, window_width=None, window_height=None):
        if background_colour is None:
            background_colour = GameConfig.DEFAULT_BACKGROUND_COLOUR
        if window_width is None:
            window_width = GameConfig.DEFAULT_WINDOW_WIDTH
        if window_height is None:
            window_height = GameConfig.DEFAULT_WINDOW_HEIGHT
        self._background_colour = Color(background_colour)
        self._window_width = window_width
        self._window_height = window_height
        return

    def get_background_colour(self):
        return self._background_colour

    def get_window_width(self):
        return self._window_width

    def get_window_height(self):
        return self._window_height
