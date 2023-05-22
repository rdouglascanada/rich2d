from game import Game, SimpleGameModel
from sprites import Circle

green_circle = Circle(rect=(100, 100, 200, 200), colour="green")
red_oval = Circle(rect=(400, 100, 150, 200), colour="red")
blue_ellipse = Circle(rect=(100, 325, 450, 200), colour="blue")
shapes = [green_circle, red_oval, blue_ellipse]
shape_game_model = SimpleGameModel(sprites=shapes)
shape_game = Game(model=shape_game_model)
shape_game.run()
