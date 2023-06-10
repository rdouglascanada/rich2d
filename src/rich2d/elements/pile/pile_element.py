from rich2d.elements import Element
from enum import Enum


class PileElement(Element):
    class PileElementDirection(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4

    def __init__(self, pile=None, direction=PileElementDirection.DOWN, spacing=0):
        if pile is None:
            raise RuntimeError("PileElement pile cannot be None")
        self._pile = pile
        self._direction = direction
        self._spacing = spacing

        def update_rects():
            pile_entries = self._pile.get_entries()
            if len(pile_entries) == 0:
                return

            top_entry = pile_entries[0]
            top_entry_rect = top_entry.get_rect()
            top_entry_rect.update(self._pile.get_rect())
            i = 1
            previous_entry_rect = top_entry_rect

            while i < len(pile_entries):
                entry_rect = pile_entries[i].get_rect()
                disp_x, disp_y = self.compute_displacement(self._spacing, self._direction)
                new_rect_values = (previous_entry_rect.x + disp_x, previous_entry_rect.y + disp_y,
                                   previous_entry_rect.w, previous_entry_rect.h)
                entry_rect.update(new_rect_values)
                previous_entry_rect = entry_rect
                i += 1

            return

        super().__init__(on_update=update_rects)
        return

    def get_pile(self):
        return self._pile

    def compute_displacement(self, spacing, direction):
        disp_x = 0
        disp_y = 0

        if spacing == 0:
            pass
        elif direction == PileElement.PileElementDirection.DOWN:
            disp_y = spacing
        elif direction == PileElement.PileElementDirection.UP:
            disp_y = -spacing
        elif direction == PileElement.PileElementDirection.LEFT:
            disp_x = -spacing
        elif direction == PileElement.PileElementDirection.RIGHT:
            disp_x = spacing
        else:
            raise RuntimeError("PileElement.compute_displacement unexpected value for direction")
        return disp_x, disp_y

