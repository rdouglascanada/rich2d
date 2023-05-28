from rich2d.game import Game
from rich2d.models import Model
from rich2d.sprites.shapes import Polygon


green_triangle = Polygon(rect=(50, 50, 100, 100), colour="green", points=((0, 1), (0.5, 0), (1, 1)))
red_triangle = Polygon(rect=(50, 50, 200, 200), colour="red", points=((0, 1), (0.5, 0), (1, 1)))
blue_rectangle = Polygon(rect=(250, 50, 100, 100), colour="blue", points=((0, 0), (1, 0), (1, 1), (0, 1)))
orange_pentagon = Polygon(rect=(350, 50, 100, 100), colour="orange",
                          points=((0, 0.25), (0.5, 0), (1, 0.25), (0.75, 1), (0.25, 1)))
purple_diamond = Polygon(rect=(450, 50, 100, 100), colour="purple", points=((0, 0.5), (0.5, 0), (1, 0.5), (0.5, 1)))

polygons = [red_triangle, green_triangle, blue_rectangle, orange_pentagon, purple_diamond]
polygon_game_model = Model(sprites=polygons)
polygon_game = Game(model=polygon_game_model)
polygon_game.run()
