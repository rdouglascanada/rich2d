import time
from rich2d.elements.element import Element


class FlashingText(Element):
    def __init__(self, text=None, text_sprite=None, flashes_per_interval=1, flash_interval=1):
        if text_sprite is None:
            raise RuntimeError("FlashingText cannot have a null text_sprite")
        if text is None:
            text = text_sprite.get_text()
        self._text_sprite = text_sprite
        self._text = text
        self._flashes_per_interval = flashes_per_interval
        self._flash_interval = flash_interval
        self._flash_timestamp = time.time()
        self._text_sprite.set_text(self._text)
        return

    def update(self):
        current_time = time.time()
        time_difference = current_time - self._flash_timestamp
        if time_difference > self._flash_interval:
            self._flash_timestamp = current_time
            time_difference = 0

        flash_flag = int(time_difference * self._flashes_per_interval / self._flash_interval * 2) % 2
        if flash_flag == 0:
            self._text_sprite.set_text(self._text)
        else:
            self._text_sprite.set_text("")
        return
