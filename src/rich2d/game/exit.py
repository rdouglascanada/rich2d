from pygame import QUIT
from pygame.event import Event, post

def exit_game():
    post(Event(QUIT))
    return