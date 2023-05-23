from .model import Model


class ModelSwitch(Model):
    def __init__(self, current_model=None):
        self._current_model = current_model
        return

    def set_current_model(self, current_model):
        self._current_model = current_model
        return

    def get_current_model(self):
        return self._current_model

    def get_handlers(self):
        if self._current_model is None:
            raise RuntimeError("ModelSwitch current_model must not be None when get_handlers() is called")
        return self._current_model.get_handlers()

    def get_sprites(self):
        if self._current_model is None:
            raise RuntimeError("ModelSwitch current_model must not be None when get_sprites() is called")
        return self._current_model.get_sprites()

    def get_elements(self):
        if self._current_model is None:
            raise RuntimeError("ModelSwitch current_model must not be None when get_elements() is called")
        return self._current_model.get_elements()
