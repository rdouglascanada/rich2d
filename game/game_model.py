from abc import ABC, abstractmethod


class GameModel(ABC):
    @abstractmethod
    def get_elements(self):
        pass

    @abstractmethod
    def get_sprites(self):
        pass


class SimpleGameModel(GameModel):
    def __init__(self, elements=[], sprites=[]):
        super().__init__()
        self._elements = tuple(elements)
        self._sprites = tuple(sprites)
        return

    def get_elements(self):
        return self._elements

    def get_sprites(self):
        return self._sprites
