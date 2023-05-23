from game import Game, GameConfig
from models import Model, Button, ModelGroup, ModelSwitch
from sprites import Rectangle, Circle


class ModelSwitchDemo(ModelSwitch):
    def __init__(self):
        super().__init__(current_model=None)
        self._rectangles_model = None
        self._circles_model = None
        return

    def switch_models(self):
        if self.get_current_model() == self._rectangles_model:
            self.set_current_model(self._circles_model)
        else:
            self.set_current_model(self._rectangles_model)
        return

    def set_rectangles_model(self, rectangles_model):
        self._rectangles_model = rectangles_model
        return

    def set_circles_model(self, circles_model):
        self._circles_model = circles_model
        return


switching_game_model = ModelSwitchDemo()


def toggle_selected_model(_):
    switching_game_model.switch_models()
    return


rectangles_background = Rectangle(rect=(0, 0, GameConfig.DEFAULT_WINDOW_WIDTH, GameConfig.DEFAULT_WINDOW_HEIGHT),
                                  colour="yellow")
green_square = Rectangle(rect=(100, 100, 200, 200), colour="green")
red_rectangle = Rectangle(rect=(400, 100, 150, 300), colour="red")

circles_background = Rectangle(rect=(0, 0, GameConfig.DEFAULT_WINDOW_WIDTH, GameConfig.DEFAULT_WINDOW_HEIGHT),
                               colour="cyan")
green_circle = Circle(rect=(100, 100, 200, 200), colour="green")
red_oval = Circle(rect=(400, 100, 150, 200), colour="red")
blue_ellipse = Circle(rect=(100, 325, 450, 200), colour="blue")

button = Button(rect=(575, 450, 150, 100), colour="gray",
                on_left_mouse_click=toggle_selected_model)

rectangles = ModelGroup(models=[Model(sprites=[rectangles_background, green_square, red_rectangle]), button])
circles = ModelGroup(models=[Model(sprites=[circles_background, green_circle, red_oval, blue_ellipse]), button])
switching_game_model.set_rectangles_model(rectangles)
switching_game_model.set_circles_model(circles)
switching_game_model.set_current_model(rectangles)

switching_game = Game(model=switching_game_model)
switching_game.run()

