from game import Game, GameConfig, SimpleGameModel
from sprites import Rectangle

background_rectangle = Rectangle(rect=(0, 0, GameConfig.DEFAULT_WINDOW_WIDTH, GameConfig.DEFAULT_WINDOW_HEIGHT),
                                 colour="yellow")
green_square = Rectangle(rect=(100, 100, 200, 200), colour="green")
red_rectangle = Rectangle(rect=(400, 100, 150, 300), colour="red")
rectangles = [background_rectangle, green_square, red_rectangle]
rectangle_game_model = SimpleGameModel(sprites=rectangles)
rectangle_game = Game(model=rectangle_game_model)
rectangle_game.run()
