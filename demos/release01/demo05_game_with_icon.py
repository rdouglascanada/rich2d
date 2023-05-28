from rich2d.game import Game, GameConfig

icon_config = GameConfig(window_icon="resources/demo05/checkmark_icon.ico")
icon_game = Game(config=icon_config)
icon_game.run()
