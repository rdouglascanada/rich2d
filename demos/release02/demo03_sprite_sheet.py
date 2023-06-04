from rich2d.game import Game, GameConfig
from rich2d.models import Model
from rich2d.sprites.images import ImageSheet, ImageSprite

w = 80
h = 120
sprite_sheet = ImageSheet(file_name="resources/demo03/cards_sprite_sheet.png", image_width=w, image_height=h)
images = sprite_sheet.get_all_images()
spades = images[0:13]
hearts = images[13:26]
clubs = images[26:39]
diamonds = images[39:52]
card_back_image = images[52]

spade_sprites = []
x = 80
y = 40
for spade_image in spades:
    spade_sprites.append(ImageSprite(image=spade_image, rect=(x, y, w, h)))
    y += 25

heart_sprites = []
x = 200
y = 40
for heart_image in hearts:
    heart_sprites.append(ImageSprite(image=heart_image, rect=(x, y, w, h)))
    y += 25

club_sprites = []
x = 320
y = 40
for club_image in clubs:
    club_sprites.append(ImageSprite(image=club_image, rect=(x, y, w, h)))
    y += 25

diamond_sprites = []
x = 440
y = 40
for diamond_image in diamonds:
    diamond_sprites.append(ImageSprite(image=diamond_image, rect=(x, y, w, h)))
    y += 25

x = 560
y = 40
card_back_sprite = [ImageSprite(image=card_back_image, rect=(x, y, w, h))]


sprites = spade_sprites + heart_sprites + club_sprites + diamond_sprites + card_back_sprite
sheet_game_model = Model(sprites=sprites)
sheet_game_config = GameConfig(window_width=800, window_height=600, background_colour="darkgreen")
sheet_game = Game(model=sheet_game_model, config=sheet_game_config)
sheet_game.run()
