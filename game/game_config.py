from pygame import Color


class GameConfig:
    DEFAULT_BACKGROUND_COLOUR = Color("black")
    DEFAULT_FRAME_RATE = 60
    DEFAULT_WINDOW_TITLE = "Rich2D Game"
    DEFAULT_WINDOW_WIDTH = 800
    DEFAULT_WINDOW_HEIGHT = 600

    def __init__(self, background_colour=None, frame_rate=None, window_title=None, window_width=None, window_height=None):
        if background_colour is None:
            background_colour = GameConfig.DEFAULT_BACKGROUND_COLOUR
        if frame_rate is None:
            frame_rate = GameConfig.DEFAULT_FRAME_RATE
        if window_title is None:
            window_title = GameConfig.DEFAULT_WINDOW_TITLE
        if window_width is None:
            window_width = GameConfig.DEFAULT_WINDOW_WIDTH
        if window_height is None:
            window_height = GameConfig.DEFAULT_WINDOW_HEIGHT
        self._background_colour = Color(background_colour)
        self._frame_rate = frame_rate
        self._window_title = window_title
        self._window_width = window_width
        self._window_height = window_height
        return

    def get_background_colour(self):
        return self._background_colour

    def get_frame_rate(self):
        return self._frame_rate

    def get_window_title(self):
        return self._window_title

    def get_window_width(self):
        return self._window_width

    def get_window_height(self):
        return self._window_height
