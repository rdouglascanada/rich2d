from pygame import Color


class GameConfig:
    DEFAULT_BACKGROUND_COLOUR = Color("black")

    def __init__(self, background_colour=None):
        if background_colour is None:
            background_colour = GameConfig.DEFAULT_BACKGROUND_COLOUR
        self._background_colour = Color(background_colour)
        return

    def get_background_colour(self):
        return self._background_colour
