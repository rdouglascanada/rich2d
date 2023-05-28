from rich2d.game import Game
from rich2d.models import Model
from rich2d.elements.animated_text import FlashingText
from rich2d.sprites import Text

flashing_text = Text(rect=(100, 100, 500, 50), text="Some flashing text", colour="white", font_size=32)
flashing_text_model = FlashingText(text_sprite=flashing_text)
faster_flashing_text = Text(rect=(100, 200, 500, 50), text="Some faster flashing text", colour="white", font_size=32)
faster_flashing_text_model = FlashingText(text_sprite=faster_flashing_text, flashes_per_interval=2)
slower_flashing_text = Text(rect=(100, 300, 500, 50), text="Some slower flashing text", colour="white", font_size=32)
slower_flashing_text_model = FlashingText(text_sprite=slower_flashing_text, flashes_per_interval=2, flash_interval=4)

text = [flashing_text, faster_flashing_text, slower_flashing_text]
text_models = [flashing_text_model, faster_flashing_text_model, slower_flashing_text_model]

text_game_model = Model(elements=text_models, sprites=text)
text_game = Game(model=text_game_model)
text_game.run()
