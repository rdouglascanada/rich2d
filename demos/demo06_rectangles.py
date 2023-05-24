from game import Game, GameConfig
from models import Model
from sprites.shapes import Rectangle

background_rectangle = Rectangle(rect=(0, 0, GameConfig.DEFAULT_WINDOW_WIDTH, GameConfig.DEFAULT_WINDOW_HEIGHT),
                                 colour="yellow")
green_square = Rectangle(rect=(100, 100, 200, 200), colour="green")
red_rectangle = Rectangle(rect=(400, 100, 150, 300), colour="red")
rectangles = [background_rectangle, green_square, red_rectangle]
rectangle_game_model = Model(sprites=rectangles)
rectangle_game = Game(model=rectangle_game_model)
rectangle_game.run()
