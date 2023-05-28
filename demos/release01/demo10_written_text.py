from rich2d.game import Game
from rich2d.models import Model
from rich2d.elements.animated_text import WrittenText
from rich2d.sprites import Text

written_text = Text(rect=(100, 100, 500, 50), text="Some written text", colour="white", font_size=32,
                    horizontal_alignment=Text.HorizontalAlignment.LEFT)
written_text_model = WrittenText(text_sprite=written_text, write_interval=5)
faster_written_text = Text(rect=(100, 200, 500, 50), text="Some faster written text", colour="white", font_size=32,
                           horizontal_alignment=Text.HorizontalAlignment.LEFT)
faster_written_text_model = WrittenText(text_sprite=faster_written_text, write_interval=2.5)
slower_written_text = Text(rect=(100, 300, 500, 50), text="Some slower written text", colour="white", font_size=32,
                           horizontal_alignment=Text.HorizontalAlignment.LEFT)
slower_written_text_model = WrittenText(text_sprite=slower_written_text, write_interval=10)

text = [written_text, faster_written_text, slower_written_text]
text_models = [written_text_model, faster_written_text_model, slower_written_text_model]

text_game_model = Model(elements=text_models, sprites=text)
text_game = Game(model=text_game_model)
text_game.run()
