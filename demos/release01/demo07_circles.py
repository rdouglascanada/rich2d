from rich2d.game import Game
from rich2d.models import Model
from rich2d.sprites.shapes import Circle

green_circle = Circle(rect=(100, 100, 200, 200), colour="green")
red_oval = Circle(rect=(400, 100, 150, 200), colour="red")
blue_ellipse = Circle(rect=(100, 325, 450, 200), colour="blue")
shapes = [green_circle, red_oval, blue_ellipse]
shape_game_model = Model(sprites=shapes)
shape_game = Game(model=shape_game_model)
shape_game.run()
