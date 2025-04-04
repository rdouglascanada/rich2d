class Element:
    def __init__(self, on_update=lambda: None, active=True):
        self._on_update = on_update
        self._active = active
        return

    def update(self):
        if self.is_active():
            self._on_update()
        return

    def is_active(self):
        return self._active

    def set_active(self, active):
        self._active = active
        return
