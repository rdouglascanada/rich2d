from rich2d.game import Game, GameConfig
from rich2d.models import Model, ModelGroup
from rich2d.models.ui import MenuBar, MenuItem
from rich2d.sprites.shapes import Rectangle

rectangle_sprite = Rectangle(rect=(300, 200, 200, 200), colour="black")


class Colours:
    values = ["black", "red", "green", "blue", "yellow"]
    colour_index = 0

    @staticmethod
    def get_colour():
        return Colours.values[Colours.colour_index]

    @staticmethod
    def increment_colour():
        Colours.colour_index += 1
        Colours.colour_index %= len(Colours.values)
        return

    @staticmethod
    def reset_colour():
        Colours.colour_index = 0
        return


def reset():
    Colours.reset_colour()
    rect = rectangle_sprite.get_rect()
    rect.update((300, 200, 200, 200))
    rectangle_sprite.set_colour(Colours.get_colour())
    return


def colour():
    Colours.increment_colour()
    rectangle_sprite.set_colour(Colours.get_colour())
    return


def big():
    rect = rectangle_sprite.get_rect()
    old_centerx, old_centery = (rect.centerx, rect.centery)
    rect.width *= 2
    rect.height *= 2
    rect.centerx = old_centerx
    rect.centery = old_centery
    return


def small():
    rect = rectangle_sprite.get_rect()
    old_centerx, old_centery = (rect.centerx, rect.centery)
    rect.width /= 2
    rect.height /= 2
    rect.centerx = old_centerx
    rect.centery = old_centery
    return


def left():
    rect = rectangle_sprite.get_rect()
    rect.x -= 50
    return


def right():
    rect = rectangle_sprite.get_rect()
    rect.x += 50
    return


def up():
    rect = rectangle_sprite.get_rect()
    rect.y -= 50
    return


def down():
    rect = rectangle_sprite.get_rect()
    rect.y += 50
    return


menu_items = [MenuItem(label="Reset", on_select=reset),
              MenuItem(label="Colour", on_select=colour),
              MenuItem(label="Big", on_select=big),
              MenuItem(label="Small", on_select=small),
              MenuItem(label="Left", on_select=left),
              MenuItem(label="Right", on_select=right),
              MenuItem(label="Up", on_select=up),
              MenuItem(label="Down", on_select=down)]

menubar_model = MenuBar(rect=(0, 0, 800, 25), menu_items=menu_items)
rectangle_model = Model(sprites=[rectangle_sprite])
menubar_game_model = ModelGroup(models=[rectangle_model, menubar_model])
menubar_game_config = GameConfig(window_width=800, window_height=600, background_colour="white")
menubar_game = Game(model=menubar_game_model, config=menubar_game_config)
menubar_game.run()
