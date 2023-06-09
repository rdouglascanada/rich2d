from rich2d.models import Model
from rich2d.sprites.text import Text
from rich2d.handlers import MouseHandler


class MenuItem:
    def __init__(self, label="", on_select=lambda: None):
        self._label = label
        self._on_select = on_select
        return

    def get_label(self):
        return self._label

    def get_on_select(self):
        return self._on_select


class SimpleMenuItemModel(Model):
    def __init__(self, rect=None, menu_item=None):
        if rect is None:
            raise RuntimeError("SimpleMenuItemModel rect cannot be None")
        if menu_item is None:
            raise RuntimeError("SimpleMenuItemModel menu_item cannot be None")

        text_sprite = self.init_text_sprite(rect, menu_item.get_label())
        handler = MouseHandler(rect=rect, on_left_mouse_click=menu_item.get_on_select())

        super().__init__(sprites=[text_sprite], handlers=[handler])
        return

    def init_text_sprite(self, rect, label):
        return Text(rect=rect, text=label, font_name="proxima nova", font_size=24)
