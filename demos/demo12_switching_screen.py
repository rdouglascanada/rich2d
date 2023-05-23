from game import Game, GameConfig
from models import Model, Button, ModelGroup, StateModel
from state import State
from sprites import Rectangle, Circle

game_state = State(value="rectangles")


def toggle_selected_model(_):
    if game_state.get_value() == "rectangles":
        game_state.set_value("circles")
    else:
        game_state.set_value("rectangles")
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

rectangles_model = ModelGroup(models=[Model(sprites=[rectangles_background, green_square, red_rectangle]), button])
circles_model = ModelGroup(models=[Model(sprites=[circles_background, green_circle, red_oval, blue_ellipse]), button])
state_map = {'circles': circles_model, 'rectangles': rectangles_model}
switching_game_model = StateModel(state=game_state, state_map=state_map)

switching_game = Game(model=switching_game_model)
switching_game.run()
