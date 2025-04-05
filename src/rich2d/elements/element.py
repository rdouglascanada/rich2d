from time import time

class Element:
    def __init__(self, on_update=lambda: None, active=True, time_interval=None):
        self._on_update = on_update
        self._active = active
        self._time_interval = time_interval
        if time_interval is not None:
            self._time_stamp = time()
        return

    def update(self):
        should_update = True
        if self._time_interval is not None:
            current_time = time()
            time_difference = current_time - self._time_stamp
            should_update = time_difference > self._time_interval
            if should_update:
                self._time_stamp = time()

        if should_update and self.is_active():
            self._on_update()
        return

    def is_active(self):
        return self._active

    def set_active(self, active):
        self._active = active
        return
