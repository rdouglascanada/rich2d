import pygame


class Pile:
    def __init__(self, rect=None, pile_entries=[]):
        if rect is None:
            raise RuntimeError("Pile rect cannot be None")
        self._rect = pygame.Rect(rect)
        self._pile_entries = list(pile_entries)
        return

    def __len__(self):
        return len(self._pile_entries)

    def __iter__(self):
        return iter(self._pile_entries)

    def __contains__(self, item):
        return item in self._pile_entries

    def get_rect(self):
        return self._rect

    def get_entries(self):
        return tuple(self._pile_entries)

    def add(self, pile_entry):
        self._pile_entries.append(pile_entry)
        return

    def add_all(self, pile_entries):
        self._pile_entries += list(pile_entries)
        return

    def remove(self, pile_entry):
        if pile_entry not in self._pile_entries:
            raise RuntimeError("Pile.remove pile_entry not in Pile")
        entry_index = self._pile_entries.index(pile_entry)
        removed_entries = self._pile_entries[entry_index:]
        self._pile_entries = self._pile_entries[:entry_index]
        return tuple(removed_entries)

    def remove_all(self):
        removed_entries = tuple(self._pile_entries)
        self._pile_entries = []
        return tuple(removed_entries)

    def is_empty(self):
        return len(self._pile_entries) == 0







