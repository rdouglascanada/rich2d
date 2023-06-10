import pygame
from rich2d.models.model import Model
from rich2d.sprites.shapes import Rectangle
from rich2d.sprites.text import Text
from rich2d.handlers import MouseHandler
from rich2d.elements import Element


class Button(Model):
    def __init__(self, rect=None, text="", on_left_mouse_click=lambda: None, on_right_mouse_click=lambda: None):
        if rect is None:
            raise RuntimeError("Button rect cannot be None")

        self._rect = pygame.Rect(rect)
        self._text = text
        self._on_left_mouse_click = on_left_mouse_click
        self._on_right_mouse_click = on_right_mouse_click

        button_background = self.init_button_background(self._rect)
        button_text = self.init_button_text(self._rect, self._text)
        button_handler = self.init_button_handler(self._rect, self._on_left_mouse_click, self._on_right_mouse_click)
        button_element = self.init_button_element(button_background, button_text, button_handler)

        sprites = [button_background, button_text]
        handlers = [button_handler]
        elements = [button_element]
        super().__init__(sprites=sprites, elements=elements, handlers=handlers)
        return

    def init_button_background(self, rect):
        return Rectangle(rect=rect, colour="gray")

    def init_button_text(self, rect, text):
        return Text(rect=rect, text=text, colour="black",
                    font_name="helvetica", font_size=24)

    def init_button_element(self, button_background, button_text, button_handler):

        def sync_button_sprite_and_handler():
            button_background.get_rect().update(self._rect)
            button_text.get_rect().update(self._rect)
            button_text.set_text(self._text)
            return

        return Element(on_update=sync_button_sprite_and_handler)

    def init_button_handler(self, rect, on_left_mouse_click, on_right_mouse_click):
        return MouseHandler(rect=rect,
                            on_left_mouse_click=on_left_mouse_click,
                            on_right_mouse_click=on_right_mouse_click)

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        return
