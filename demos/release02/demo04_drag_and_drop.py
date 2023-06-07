from rich2d.game import Game, GameConfig
from rich2d.models import Model
from rich2d.handlers import DragAndDropHandler
from rich2d.sprites.shapes import Rectangle


green_square = Rectangle(rect=(100, 100, 200, 200), colour="green")
yellow_square = Rectangle(rect=(300, 300, 200, 200), colour="yellow")
red_square = Rectangle(rect=(500, 100, 200, 200), colour="red")


def is_yellow_release_valid():
    return yellow_square.get_rect().centerx <= 400


green_handler = DragAndDropHandler(sprite=green_square)
yellow_handler = DragAndDropHandler(sprite=yellow_square, on_release=is_yellow_release_valid)
red_handler = DragAndDropHandler(sprite=red_square, on_release=lambda: False)

sprites = [green_square, yellow_square, red_square]
handlers = [green_handler, yellow_handler, red_handler]

drag_and_drop_game_model = Model(sprites=sprites, handlers=handlers)
drag_and_drop_game_config = GameConfig(window_width=800, window_height=600, background_colour="white")
drag_and_drop_game = Game(model=drag_and_drop_game_model, config=drag_and_drop_game_config)
drag_and_drop_game.run()
