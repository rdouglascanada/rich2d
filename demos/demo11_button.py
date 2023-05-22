from game import Game
from models import Model
from sprites import Text, Rectangle
from handlers import MouseClickHandler

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


button_handler = MouseClickHandler(rect=(300, 400, 200, 200),
                                   on_left_mouse_click=toggle_text_handler(left_text_sprite),
                                   on_right_mouse_click=toggle_text_handler(right_text_sprite))
button_sprite = Rectangle(rect=(325, 400, 150, 100), colour="gray")

button_game_model = Model(sprites=[left_text_sprite, right_text_sprite, button_sprite], handlers=[button_handler])
button_game = Game(model=button_game_model)
button_game.run()

