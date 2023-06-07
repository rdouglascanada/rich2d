import pygame.mouse

from rich2d.game import Game, GameConfig
from rich2d.models import Model
from rich2d.handlers import DragAndDropHandler
from rich2d.sprites.shapes import Rectangle


green_square = Rectangle(rect=(100, 100, 200, 200), colour="green")
yellow_square = Rectangle(rect=(300, 300, 200, 200), colour="yellow")
red_square = Rectangle(rect=(500, 100, 200, 200), colour="red")


def is_not_already_dragging_another_sprite():
    return not (green_handler.is_dragging() or yellow_handler.is_dragging() or red_handler.is_dragging())


def is_yellow_release_valid():
    return yellow_square.get_rect().centerx <= 400


def on_red_square_move():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    center_x = mouse_x + (red_square.get_rect().width / 2 - 20)
    center_y = mouse_y + (red_square.get_rect().height / 2 - 20)
    return center_x, center_y


green_handler = DragAndDropHandler(sprite=green_square, on_click=is_not_already_dragging_another_sprite)
yellow_handler = DragAndDropHandler(sprite=yellow_square, on_click=is_not_already_dragging_another_sprite,
                                    on_release=is_yellow_release_valid)
red_handler = DragAndDropHandler(sprite=red_square, on_click=is_not_already_dragging_another_sprite,
                                 on_move=on_red_square_move, on_release=lambda: False)

sprites = [green_square, yellow_square, red_square]
handlers = [red_handler, yellow_handler, green_handler]

drag_and_drop_game_model = Model(sprites=sprites, handlers=handlers)
drag_and_drop_game_config = GameConfig(window_width=800, window_height=600, background_colour="white")
drag_and_drop_game = Game(model=drag_and_drop_game_model, config=drag_and_drop_game_config)
drag_and_drop_game.run()
