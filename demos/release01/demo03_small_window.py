from rich2d.game import Game, GameConfig

small_config = GameConfig(window_width=400, window_height=400)
small_game = Game(config=small_config)
small_game.run()
