from rich2d.game import Game, GameConfig
from rich2d.models import Model
from rich2d.sprites.images import Image, ImageSprite

tux_image = Image.load_from_file("resources/demo01/tux.png")
windows_image = Image.load_from_file("resources/demo01/windows.png")
apple_image = Image.load_from_file("resources/demo01/apple.png")

small_image_sprite = ImageSprite(image=tux_image, rect=(50, 50, 100, 100))
medium_image_sprite = ImageSprite(image=tux_image, rect=(200, 50, 200, 300))
big_image_sprite = ImageSprite(image=tux_image, rect=(450, 50, 350, 300))
windows_image_sprite = ImageSprite(image=windows_image, rect=(50, 350, 325, 250))
apple_image_sprite = ImageSprite(image=apple_image, rect=(425, 350, 325, 250))

image_game_model = Model(sprites=[small_image_sprite, medium_image_sprite, big_image_sprite,
                                  windows_image_sprite, apple_image_sprite])
image_game_config = GameConfig(window_width=800, window_height=600, background_colour="white")
image_game = Game(model=image_game_model, config=image_game_config)
image_game.run()
