from .model import Model


class ModelGroup(Model):
    def __init__(self, models=[]):
        elements = tuple()
        sprites = tuple()
        handlers = tuple()

        for model in models:
            elements += tuple(model.get_elements())
            sprites += tuple(model.get_sprites())
            handlers += tuple(model.get_handlers())

        super().__init__(elements=elements, sprites=sprites, handlers=handlers)
        return
