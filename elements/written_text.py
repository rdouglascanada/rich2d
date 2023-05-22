import time
from .element import Element


class WrittenText(Element):
    def __init__(self, text=None, text_sprite=None, write_interval=1):
        if text_sprite is None:
            raise RuntimeError("WrittenText cannot have a null text_sprite")
        if text is None:
            text = text_sprite.get_text()
        self._text_sprite = text_sprite
        self._text = text
        self._write_interval = write_interval
        self._write_timestamp = time.time()
        self._text_sprite.set_text(self._text)
        return

    def reset(self):
        self._write_timestamp = time.time()
        return

    def update(self):
        current_time = time.time()
        time_difference = current_time - self._write_timestamp
        if time_difference > self._write_interval:
            chars_to_display = len(self._text)
        else:
            chars_to_display = int(time_difference / self._write_interval * len(self._text))
        self._text_sprite.set_text(self._text[:chars_to_display])
        return
