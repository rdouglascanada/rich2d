import pygame
from .handler import Handler


class MouseHandler(Handler):
    def __init__(self, rect=None,
                 on_left_mouse_click=lambda: None, on_right_mouse_click=lambda: None):
        if rect is not None:
            rect = pygame.Rect(rect)
        self._rect = rect
        self._on_left_mouse_click = on_left_mouse_click
        self._on_right_mouse_click = on_right_mouse_click
        return

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect is None or self._rect.collidepoint(event.pos):
                if event.button == pygame.BUTTON_LEFT:
                    self._on_left_mouse_click()
                elif event.button == pygame.BUTTON_RIGHT:
                    self._on_right_mouse_click()
        return

