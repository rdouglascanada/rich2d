from game import Game
from models import Model, Button
from sprites import Text

left_text_sprite = Text(rect=(100, 100, 300, 50), text="Some text", colour="white", font_size=32)
right_text_sprite = Text(rect=(100, 200, 300, 50), text="Some other text", colour="white", font_size=32)


def toggle_text_handler(text_sprite):
    full_text = text_sprite.get_text()

    def handler(_):
        if text_sprite.get_text() == "":
            text_sprite.set_text(full_text)
        else:
            text_sprite.set_text("")
        return
    return handler


button = Button(rect=(325, 400, 150, 100), colour="gray",
                on_left_mouse_click=toggle_text_handler(left_text_sprite),
                on_right_mouse_click=toggle_text_handler(right_text_sprite))

button_game_model = Model(sprites=tuple([left_text_sprite, right_text_sprite]) + button.get_sprites(),
                          elements=button.get_elements(), handlers=button.get_handlers())
button_game = Game(model=button_game_model)
button_game.run()

