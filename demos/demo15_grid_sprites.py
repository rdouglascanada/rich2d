from game import Game
from models import Model
from sprites.shapes import Rectangle, Circle, Polygon
from elements.grid import Grid, GridElement

grid = Grid(grid_rect=(0, 0, 800, 600), rows=6, columns=8)

background_rectangle = Rectangle(rect=(0, 0, 0, 0), colour="cyan")
background_rectangle_element = GridElement(sprite=background_rectangle, grid=grid,
                                           x_index=0, y_index=0, x_tiles=8, y_tiles=6)
green_rectangle = Rectangle(rect=(0, 0, 0, 0), colour="green")
green_rectangle_element = GridElement(sprite=green_rectangle, grid=grid,
                                      x_index=1, y_index=1, x_tiles=4, y_tiles=1)
blue_circle = Circle(rect=(0, 0, 0, 0), colour="blue")
blue_circle_element = GridElement(sprite=blue_circle, grid=grid,
                                  x_index=5, y_index=3, x_tiles=2, y_tiles=2)
red_triangle = Polygon(rect=(0, 0, 0, 0), colour="red", points=((0, 1), (0.5, 0), (1, 1)))
red_triangle_element = GridElement(sprite=red_triangle, grid=grid,
                                   x_index=1, y_index=4, x_tiles=4, y_tiles=2)

sprites = [background_rectangle, green_rectangle, blue_circle, red_triangle]
elements = [background_rectangle_element, green_rectangle_element, blue_circle_element, red_triangle_element]

grid_game_model = Model(sprites=sprites, elements=elements)
grid_game = Game(model=grid_game_model)
grid_game.run()
