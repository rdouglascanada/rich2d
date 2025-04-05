from rich2d.elements.element import Element


class FlashingText(Element):
    def __init__(self, text_sprite=None, flashes_per_interval=1, flash_interval=1):
        if text_sprite is None:
            raise RuntimeError("FlashingText cannot have a null text_sprite")

        def on_update():
            text_sprite.set_visible(not text_sprite.is_visible())
            return

        time_interval = flash_interval / (flashes_per_interval * 2)
        super().__init__(on_update=on_update, time_interval=time_interval)
        return
