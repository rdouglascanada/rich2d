import pygame
from game import Game, GameConfig
from models import Model, StateModel
from models.state import State
from sprites import Text
from handlers import KeyboardHandler
from elements.animated_text import FlashingText

game_state = State(value="title")


def start_game():
    game_state.set_value("game")
    return


def back_to_title():
    game_state.set_value("title")
    return


title_text = Text(rect=(0, 0, 800, 600),
                  text="Game Title", colour="black", font_name="Arial",  font_size=100, font_bold=True)
spacebar_text = Text(rect=(0, 500, 800, 100),
                     text="Press spacebar to start game", colour="black", font_size=32, font_italic=True)
flashing_text = FlashingText(text_sprite=spacebar_text, flashes_per_interval=3, flash_interval=4)
title_handler = KeyboardHandler(key_pressed_map={pygame.K_SPACE: start_game})
title_model = Model(sprites=[title_text, spacebar_text], elements=[flashing_text], handlers=[title_handler])

game_return_text = Text(rect=(0, 500, 800, 100),
                        text="Press enter to go back to title", colour="black", font_size=32)
game_handler = KeyboardHandler(key_pressed_map={pygame.K_RETURN: back_to_title})
game_model = Model(sprites=[game_return_text], handlers=[game_handler])

state_map = {'title': title_model, 'game': game_model}
keypress_game_model = StateModel(state=game_state, state_map=state_map)
keypress_game_config = GameConfig(background_colour="white", window_width=800, window_height=600)
keypress_game = Game(model=keypress_game_model, config=keypress_game_config)
keypress_game.run()
