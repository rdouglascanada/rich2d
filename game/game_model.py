from abc import ABC, abstractmethod


class GameModel(ABC):
    @abstractmethod
    def get_sprites(self):
        pass


class SimpleGameModel(GameModel):
    def __init__(self, sprites=[]):
        super().__init__()
        self._sprites = tuple(sprites)
        return

    def get_sprites(self):
        return self._sprites
