from rich2d.elements.element import Element


class WrittenText(Element):
    def __init__(self, text=None, text_sprite=None, write_interval=1):
        if text_sprite is None:
            raise RuntimeError("WrittenText cannot have a null text_sprite")
        if text is None:
            text = text_sprite.get_text()
        text_sprite.set_text("")
        self._chars_to_display = 0

        def on_update():
            self._chars_to_display += 1
            text_sprite.set_text(text[:self._chars_to_display])
            return

        time_interval = write_interval / len(text)
        super().__init__(on_update=on_update, time_interval=time_interval)
        return
