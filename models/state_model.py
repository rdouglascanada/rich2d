from .model import Model


class StateModel(Model):
    def __init__(self, state=None, state_map=None):
        if state is None:
            raise RuntimeError("StateModel cannot be initialized without state")
        if state_map is None:
            raise RuntimeError("StateModel cannot be initialized without state_map")
        self._state = state
        self._state_map = state_map
        return

    def get_sprites(self):
        return self._state_map[self._state.get_value()].get_sprites()

    def get_handlers(self):
        return self._state_map[self._state.get_value()].get_handlers()

    def get_elements(self):
        return self._state_map[self._state.get_value()].get_elements()
