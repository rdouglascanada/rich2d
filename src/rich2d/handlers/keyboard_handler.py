import pygame
from .handler import Handler


class KeyboardHandler(Handler):
    def __init__(self, key_pressed_map={}, key_released_map={}):
        self._key_pressed_map = key_pressed_map
        self._key_released_map = key_released_map
        return

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self._key_pressed_map.keys():
                self._key_pressed_map[event.key]()
        if event.type == pygame.KEYUP:
            if event.key in self._key_released_map.keys():
                self._key_released_map[event.key]()
        return
