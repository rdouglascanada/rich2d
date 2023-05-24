import pygame
from game import Game, GameConfig
from models import Model
from sprites import Text
from sprites.shapes import Rectangle
from handlers import KeyboardHandler
from elements.grid import Grid, GridElement

grid = Grid(rect=(0, 0, 600, 600), rows=20, columns=20)

background_rectangle = Rectangle(rect=(0, 0, 0, 0), colour="yellow")
background_rectangle_element = GridElement(sprite=background_rectangle, grid=grid,
                                           grid_tiles=(0, 0, 20, 20))
top_boundary = Rectangle(rect=(0, 0, 0, 0), colour="black")
top_boundary_element = GridElement(sprite=top_boundary, grid=grid,
                                   grid_tiles=(0, 0, 20, 1))
left_boundary = Rectangle(rect=(0, 0, 0, 0), colour="black")
left_boundary_element = GridElement(sprite=left_boundary, grid=grid,
                                    grid_tiles=(0, 1, 1, 18))
right_boundary = Rectangle(rect=(0, 0, 0, 0), colour="black")
right_boundary_element = GridElement(sprite=right_boundary, grid=grid,
                                     grid_tiles=(19, 1, 1, 18))
bottom_boundary = Rectangle(rect=(0, 0, 0, 0), colour="black")
bottom_boundary_element = GridElement(sprite=bottom_boundary, grid=grid,
                                      grid_tiles=(0, 19, 20, 1))

moving_rectangle = Rectangle(rect=(0, 0, 0, 0), colour="blue")
moving_rectangle_element = GridElement(sprite=moving_rectangle, grid=grid,
                                       grid_tiles=(9, 9, 3, 2))

bottom_background_rectangle = Rectangle(rect=(0, 600, 600, 100), colour="white")
instruction_text = Text(rect=(0, 600, 600, 100), text="Move the blue rectangle using the arrow keys", colour="blue",
                        font_size=20, horizontal_alignment=Text.HorizontalAlignment.CENTRE)


def handle_up_arrow():
    grid_tiles = moving_rectangle_element.get_grid_tiles()
    grid_tiles.set_y_index(grid_tiles.get_y_index() - 1)
    boundary_tiles = top_boundary_element.get_grid_tiles()
    if boundary_tiles.collides_with(grid_tiles):
        grid_tiles.set_y_index(grid_tiles.get_y_index() + 1)
    return


def handle_down_arrow():
    grid_tiles = moving_rectangle_element.get_grid_tiles()
    grid_tiles.set_y_index(grid_tiles.get_y_index() + 1)
    boundary_tiles = bottom_boundary_element.get_grid_tiles()
    if boundary_tiles.collides_with(grid_tiles):
        grid_tiles.set_y_index(grid_tiles.get_y_index() - 1)
    return


def handle_left_arrow():
    grid_tiles = moving_rectangle_element.get_grid_tiles()
    grid_tiles.set_x_index(grid_tiles.get_x_index() - 1)
    boundary_tiles = left_boundary_element.get_grid_tiles()
    if boundary_tiles.collides_with(grid_tiles):
        grid_tiles.set_x_index(grid_tiles.get_x_index() + 1)
    return


def handle_right_arrow():
    grid_tiles = moving_rectangle_element.get_grid_tiles()
    grid_tiles.set_x_index(grid_tiles.get_x_index() + 1)
    boundary_tiles = right_boundary_element.get_grid_tiles()
    if boundary_tiles.collides_with(grid_tiles):
        grid_tiles.set_x_index(grid_tiles.get_x_index() - 1)
    return


key_pressed_map = {pygame.K_UP: handle_up_arrow, pygame.K_DOWN: handle_down_arrow,
                   pygame.K_LEFT: handle_left_arrow, pygame.K_RIGHT: handle_right_arrow}
keyboard_handler = KeyboardHandler(key_pressed_map=key_pressed_map)

sprites = [background_rectangle, top_boundary, left_boundary, right_boundary, bottom_boundary, moving_rectangle,
           bottom_background_rectangle, instruction_text]
elements = [background_rectangle_element, top_boundary_element, left_boundary_element,
            right_boundary_element, bottom_boundary_element, moving_rectangle_element]
handlers = [keyboard_handler]

grid_game_config = GameConfig(window_width=600, window_height=700)
grid_game_model = Model(sprites=sprites, elements=elements, handlers=handlers)
grid_game = Game(model=grid_game_model, config=grid_game_config)
grid_game.run()
