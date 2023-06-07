import pygame
from rich2d.handlers import MouseHandler


class DragAndDropHandler(MouseHandler):
    def __init__(self,
                 sprite=None,
                 on_click=lambda: True,
                 on_move=lambda: pygame.mouse.get_pos(),
                 on_release=lambda: True):
        if sprite is None:
            raise RuntimeError("DragAndDropModel tracked_sprite cannot be None")
        self._sprite = sprite
        self._original_rect = pygame.Rect(sprite.get_rect())
        self._dragging = False

        def on_mouse_click():
            self._dragging = on_click()
            return

        def on_mouse_move():
            if self._dragging:
                mouse_x, mouse_y = on_move()
                for rect in [sprite.get_rect(), self.get_rect()]:
                    rect.centerx = mouse_x
                    rect.centery = mouse_y
            return

        def on_mouse_release():
            if self._dragging:
                self._dragging = False
                valid_destination = on_release()
                if not valid_destination:
                    for rect in [sprite.get_rect(), self.get_rect()]:
                        rect.update(self._original_rect)
                else:
                    self._original_rect.update(sprite.get_rect())
            return

        super().__init__(rect=sprite.get_rect(),
                         on_left_mouse_click=on_mouse_click,
                         on_mouse_move=on_mouse_move,
                         on_left_mouse_release=on_mouse_release,
                         override_mouse_move_rect=True,
                         override_left_mouse_release_rect=True)
        return

    def is_dragging(self):
        return self._dragging
