import pygame
from .handler import Handler


class MouseHandler(Handler):
    def __init__(self, rect=None,
                 on_left_mouse_click=lambda: None,
                 on_right_mouse_click=lambda: None,
                 on_left_mouse_release=lambda: None,
                 on_right_mouse_release=lambda: None,
                 on_mouse_move=lambda: None,
                 override_left_mouse_click_rect=False,
                 override_right_mouse_click_rect=False,
                 override_left_mouse_release_rect=False,
                 override_right_mouse_release_rect=False,
                 override_mouse_move_rect=False):
        if rect is not None:
            rect = pygame.Rect(rect)
        self._rect = rect

        self._on_left_mouse_click = on_left_mouse_click
        self._on_right_mouse_click = on_right_mouse_click
        self._on_left_mouse_release = on_left_mouse_release
        self._on_right_mouse_release = on_right_mouse_release
        self._on_mouse_move = on_mouse_move

        self._override_left_mouse_click_rect = override_left_mouse_click_rect
        self._override_right_mouse_click_rect = override_right_mouse_click_rect
        self._override_left_mouse_release_rect = override_left_mouse_release_rect
        self._override_right_mouse_release_rect = override_right_mouse_release_rect
        self._override_mouse_move_rect = override_mouse_move_rect
        return

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if self._rect is None or self._override_left_mouse_click_rect or self._rect.collidepoint(event.pos):
                    self._on_left_mouse_click()
            elif event.button == pygame.BUTTON_RIGHT:
                if self._rect is None or self._override_right_mouse_click_rect or self._rect.collidepoint(event.pos):
                    self._on_right_mouse_click()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self._rect is None or self._override_left_mouse_release_rect or self._rect.collidepoint(event.pos):
                    self._on_left_mouse_release()
            elif event.button == pygame.BUTTON_RIGHT:
                if self._rect is None or self._override_right_mouse_release_rect or self._rect.collidepoint(event.pos):
                    self._on_right_mouse_release()
        elif event.type == pygame.MOUSEMOTION:
            if self._rect is None or self._override_mouse_move_rect or self._rect.collidepoint(event.pos):
                self._on_mouse_move()
        return

    def get_rect(self):
        return self._rect

