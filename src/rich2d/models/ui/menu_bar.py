import pygame
from rich2d.models import Model, ModelGroup
from rich2d.sprites.shapes import Rectangle
from .menu_item import SimpleMenuItemModel


class MenuBar(ModelGroup):
    def __init__(self, rect=None, menu_items=[], max_menu_items=10):
        if rect is None:
            raise RuntimeError("MenuBar rect cannot be None")
        if len(menu_items) > max_menu_items:
            raise RuntimeError("MenuBar: Number of menu items cannot be larger than max_menu_items")
        rect = pygame.Rect(rect)
        self._rect = rect
        self._menu_items = tuple(menu_items)
        self._max_menu_items = max_menu_items

        background = self.init_background(rect)
        background_model = Model(sprites=[background])
        
        menu_item_models = []
        i = 0
        x = rect.x
        y = rect.y
        w = rect.w // max_menu_items
        h = rect.h
        while i < len(menu_items):
            menu_item = menu_items[i]
            menu_item_model = self.init_menu_item((x, y, w, h), menu_item)
            menu_item_models.append(menu_item_model)
            x += w
            i += 1
            
        super().__init__(models=[background_model] + menu_item_models)
        return

    def get_rect(self):
        return self._rect

    def init_background(self, rect):
        return Rectangle(rect=rect, colour="darkgray")

    def init_menu_item(self, rect, menu_item):
        return SimpleMenuItemModel(rect=rect, menu_item=menu_item)
