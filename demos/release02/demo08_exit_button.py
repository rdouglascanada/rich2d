from rich2d.game import Game, exit_game
from rich2d.models import Button

def quit_game():
    print("Game exited successfully")
    exit_game()
    return

button = Button(rect=(100, 250, 600, 100),
                text="Left/Right Click to Quit Game",
                on_left_mouse_click=quit_game,
                on_right_mouse_click=quit_game)
button_game = Game(model=button)
button_game.run()

