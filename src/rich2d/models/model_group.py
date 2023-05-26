from .model import Model


class ModelGroup(Model):
    def __init__(self, models=[]):
        self._models = models
        return

    def get_sprites(self):
        sprites = tuple()
        for model in self._models:
            sprites += tuple(model.get_sprites())
        return sprites

    def get_elements(self):
        elements = tuple()
        for model in self._models:
            elements += tuple(model.get_elements())
        return elements

    def get_handlers(self):
        handlers = tuple()
        for model in self._models:
            handlers += tuple(model.get_handlers())
        return handlers
