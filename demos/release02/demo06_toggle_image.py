from rich2d.game import Game, GameConfig
from rich2d.models import Model, ModelGroup
from rich2d.models.ui import Button
from rich2d.sprites.images import Image, ImageSprite

card_image = Image.load_from_file("resources/demo06/card.png")
card_back_image = Image.load_from_file("resources/demo06/card_back.png")

card_image_sprite = ImageSprite(image=card_back_image, rect=(50, 50, 160, 240))


def toggle_image():
    if card_image_sprite.get_image() == card_image:
        card_image_sprite.set_image(card_back_image)
        button.set_text("Show Card")
    else:
        card_image_sprite.set_image(card_image)
        button.set_text("Hide Card")
    return


button = Button(rect=(50, 310, 160, 40), text="Show Card", on_left_mouse_click=toggle_image)

sprites = [card_image_sprite]
card_model = Model(sprites=sprites)

toggle_game_config = GameConfig(window_width=800, window_height=600, background_colour="darkgreen")
toggle_game_model = ModelGroup(models=[card_model, button])
toggle_game = Game(model=toggle_game_model, config=toggle_game_config)
toggle_game.run()
