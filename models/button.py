import pygame
from .model import Model
from sprites.shapes import Rectangle
from sprites import Text
from handlers import MouseHandler
from elements import Element


class Button(Model):
    DEFAULT_COLOUR = pygame.Color("gray")
    DEFAULT_FONT_COLOUR = pygame.Color("black")
    DEFAULT_FONT_SIZE = 24

    def __init__(self, rect=None, colour=None, text="", font_colour=None,
                 font=None, font_name=None, font_size=None, font_bold=True, font_italic=False,
                 on_left_mouse_click=lambda: None, on_right_mouse_click=lambda: None):
        if rect is None:
            raise RuntimeError("Button rect cannot be None")
        if colour is None:
            colour = Button.DEFAULT_COLOUR
        if font_colour is None:
            font_colour = Button.DEFAULT_FONT_COLOUR
        if font_size is None:
            font_size = Button.DEFAULT_FONT_SIZE

        self._rect = pygame.Rect(rect)
        self._colour = pygame.Color(colour)
        self._font_colour = pygame.Color(font_colour)
        self._text = text
        self._on_left_mouse_click = on_left_mouse_click
        self._on_right_mouse_click = on_right_mouse_click

        button_rectangle = Rectangle(rect=self._rect, colour=self._colour)
        button_text = Text(rect=self._rect, text=self._text, colour=self._font_colour,
                           font=font, font_name=font_name, font_size=font_size,
                           font_bold=font_bold, font_italic=font_italic)
        button_handler = MouseHandler(rect=self._rect,
                                      on_left_mouse_click=self._on_left_mouse_click,
                                      on_right_mouse_click=self._on_right_mouse_click)

        def sync_button_sprite_and_handler():
            button_rectangle.get_rect().update(self._rect)
            button_rectangle.set_colour(self._colour)
            button_text.get_rect().update(self._rect)
            button_text.set_colour(self._font_colour)
            button_text.set_text(self._text)
            return
        button_element = Element(on_update=sync_button_sprite_and_handler)

        elements = [button_element]
        sprites = [button_rectangle, button_text]
        handlers = [button_handler]
        super().__init__(sprites=sprites, elements=elements, handlers=handlers)
        return
