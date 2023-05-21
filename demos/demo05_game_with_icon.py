from game import Game, GameConfig

icon_config = GameConfig(window_icon="../resources/demo05/example_icon.jpg")
icon_game = Game(config=icon_config)
icon_game.start()
