from rich2d.game import Game, GameConfig
from rich2d.models import Model
from rich2d.elements.pile import Pile, PileElement
from rich2d.sprites.images import Image, ImageSprite

card_back_image = Image.load_from_file("resources/demo07/card_back.png")

card_sprites = []
pile_elements = []

pile1 = Pile(rect=(50, 50, 80, 120))
pile1_element = PileElement(pile=pile1, spacing=20)
pile_elements.append(pile1_element)

for i in range(8):
    sprite = ImageSprite(image=card_back_image, rect=(0, 0, 0, 0))
    card_sprites.append(sprite)
    pile1.add(sprite)

pile2 = Pile(rect=(150, 250, 80, 120))
pile2_element = PileElement(pile=pile2, spacing=30, direction=PileElement.PileElementDirection.UP)
pile_elements.append(pile2_element)

for i in range(8):
    sprite = ImageSprite(image=card_back_image, rect=(0, 0, 0, 0))
    card_sprites.append(sprite)
    pile2.add(sprite)

pile3 = Pile(rect=(250, 50, 80, 120))
pile3_element = PileElement(pile=pile3, spacing=40, direction=PileElement.PileElementDirection.RIGHT)
pile_elements.append(pile3_element)

for i in range(12):
    sprite = ImageSprite(image=card_back_image, rect=(0, 0, 0, 0))
    card_sprites.append(sprite)
    pile3.add(sprite)

pile4 = Pile(rect=(670, 250, 80, 120))
pile4_element = PileElement(pile=pile4, spacing=35, direction=PileElement.PileElementDirection.LEFT)
pile_elements.append(pile4_element)

for i in range(12):
    sprite = ImageSprite(image=card_back_image, rect=(0, 0, 0, 0))
    card_sprites.append(sprite)
    pile4.add(sprite)

pile5 = Pile(rect=(360, 450, 80, 120))
pile5_element = PileElement(pile=pile5, spacing=0)
pile_elements.append(pile5_element)

for i in range(12):
    sprite = ImageSprite(image=card_back_image, rect=(0, 0, 0, 0))
    card_sprites.append(sprite)
    pile5.add(sprite)

pile_game_config = GameConfig(window_width=800, window_height=600, background_colour="darkgreen")
pile_game_model = Model(sprites=card_sprites, elements=pile_elements)
pile_game = Game(model=pile_game_model, config=pile_game_config)
pile_game.run()
