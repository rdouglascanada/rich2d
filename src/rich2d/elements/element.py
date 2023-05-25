class Element:
    def __init__(self, on_update=lambda: None):
        self._on_update = on_update
        return

    def update(self):
        self._on_update()
        return
