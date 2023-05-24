from game import Game, GameConfig
from models import Model
from sprites.shapes import Rectangle, Circle, Polygon
from elements.grid import Grid, GridElement

grid = Grid(rect=(0, 0, 800, 600), rows=6, columns=8)

background_rectangle = Rectangle(rect=(0, 0, 0, 0), colour="cyan")
background_rectangle_element = GridElement(sprite=background_rectangle, grid=grid,
                                           grid_tiles=(0, 0, 8, 6))
green_rectangle = Rectangle(rect=(0, 0, 0, 0), colour="green")
green_rectangle_element = GridElement(sprite=green_rectangle, grid=grid,
                                      grid_tiles=(1, 1, 4, 1))
blue_circle = Circle(rect=(0, 0, 0, 0), colour="blue")
blue_circle_element = GridElement(sprite=blue_circle, grid=grid,
                                  grid_tiles=(5, 3, 2, 2))
red_triangle = Polygon(rect=(0, 0, 0, 0), colour="red", points=((0, 1), (0.5, 0), (1, 1)))
red_triangle_element = GridElement(sprite=red_triangle, grid=grid,
                                   grid_tiles=(1, 4, 4, 2))

sprites = [background_rectangle, green_rectangle, blue_circle, red_triangle]
elements = [background_rectangle_element, green_rectangle_element, blue_circle_element, red_triangle_element]

grid_game_config = GameConfig(window_width=800, window_height=600)
grid_game_model = Model(sprites=sprites, elements=elements)
grid_game = Game(model=grid_game_model, config=grid_game_config)
grid_game.run()
