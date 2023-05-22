import pygame
from .model import Model
from sprites import Rectangle
from handlers import MouseClickHandler
from elements import Element


class Button(Model):
    DEFAULT_COLOUR = pygame.Color("gray")

    def __init__(self, rect=None, colour=None,
                 on_left_mouse_click=lambda event: None, on_right_mouse_click=lambda event: None):
        if rect is None:
            raise RuntimeError("Button rect cannot be None")
        if colour is None:
            colour = Button.DEFAULT_COLOUR

        self._rect = pygame.Rect(rect)
        self._colour = pygame.Color(colour)
        self._on_left_mouse_click = on_left_mouse_click
        self._on_right_mouse_click = on_right_mouse_click

        button_rectangle = Rectangle(rect=self._rect, colour=self._colour)
        button_handler = MouseClickHandler(rect=self._rect,
                                           on_left_mouse_click=self._on_left_mouse_click,
                                           on_right_mouse_click=self._on_right_mouse_click)

        def sync_button_sprite_and_handler():
            button_rectangle.get_rect().update(self._rect)
            button_rectangle.set_colour(self._colour)
            return
        button_element = Element(on_update=sync_button_sprite_and_handler)

        elements = [button_element]
        sprites = [button_rectangle]
        handlers = [button_handler]
        super().__init__(sprites=sprites, elements=elements, handlers=handlers)
        return
