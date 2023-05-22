from game import Game, SimpleGameModel
from sprites import Text

white_text = Text(rect=(100, 100, 300, 50), text="Some simple text", colour="white", font_size=32)
arial_text = Text(rect=(100, 150, 300, 50), text="Some arial text", colour="red", font_size=32, font_name="arial")
big_bold_arial_text = Text(rect=(100, 200, 300, 50), text="Some big bold arial text", colour="blue",
                           font_size=48, font_name="arial", font_bold=True)
small_italic_text = Text(rect=(100, 275, 300, 50), text="Some small italic text", colour="green",
                         font_size=20, font_italic=True)


text = [white_text, arial_text, big_bold_arial_text, small_italic_text]
text_game_model = SimpleGameModel(sprites=text)
text_game = Game(model=text_game_model)
text_game.run()
