from rich2d.game import Game, GameConfig
from rich2d.models import ModelGroup, Model
from rich2d.elements import Element
from rich2d.models.ui import Button
from rich2d.sprites.text import ScaledText

class NumberModel(ModelGroup):
    def __init__(self):

        text_sprite = ScaledText(text="", rect=(0, 0, 800, 300))

        class Globals:
            increasing_number = 0

        def increase_number():
            Globals.increasing_number += 1
            text_sprite.set_text(str(Globals.increasing_number))
            return

        text_element = Element(on_update=increase_number)

        def toggle_visibility():
            text_sprite.set_visible(not text_sprite.is_visible())
            return

        def toggle_activity():
            text_element.set_active(not text_element.is_active())
            return

        def toggle_both():
            toggle_visibility()
            toggle_activity()
            return

        visibility_button = Button(rect=(300, 315, 200, 80),
                                   text="Toggle Visibility",
                                   on_left_mouse_click=toggle_visibility)

        activity_button = Button(rect=(300, 410, 200, 80),
                                   text="Toggle Activity",
                                   on_left_mouse_click=toggle_activity)

        both_button = Button(rect=(300, 505, 200, 80),
                             text="Toggle Both",
                             on_left_mouse_click=toggle_both)

        super().__init__(models=[Model(sprites=[text_sprite], elements=[text_element]),
                                 visibility_button, activity_button, both_button])
        return

config = GameConfig(window_title="Visibility & Activity Demo", background_colour="white",
                    window_width=800, window_height=600)
game = Game(model=NumberModel(), config=config)
game.run()