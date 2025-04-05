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

        text_element = Element(on_update=increase_number, active=False, time_interval=1)

        def start_count():
            text_element.set_active(True)
            return

        def stop_count():
            text_element.set_active(False)
            return

        def reset_count():
            text_element.set_active(False)
            Globals.increasing_number = 0
            text_sprite.set_text("")
            return

        start_button = Button(rect=(300, 315, 200, 80),
                                   text="Start Counting",
                                   on_left_mouse_click=start_count)

        stop_button = Button(rect=(300, 410, 200, 80),
                                   text="Stop Counting",
                                   on_left_mouse_click=stop_count)

        reset_button = Button(rect=(300, 505, 200, 80),
                             text="Reset",
                             on_left_mouse_click=reset_count)

        super().__init__(models=[Model(sprites=[text_sprite], elements=[text_element]),
                                 start_button, stop_button, reset_button])
        return

config = GameConfig(window_title="Time Interval Demo", background_colour="white",
                    window_width=800, window_height=600)
game = Game(model=NumberModel(), config=config)
game.run()