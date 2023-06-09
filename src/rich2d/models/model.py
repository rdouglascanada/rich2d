class Model:
    def __init__(self, elements=[], sprites=[], handlers=[]):
        super().__init__()
        self._elements = tuple(elements)
        self._sprites = tuple(sprites)
        self._handlers = tuple(handlers)
        return

    def get_elements(self):
        return self._elements

    def get_sprites(self):
        return self._sprites

    def get_handlers(self):
        return self._handlers
