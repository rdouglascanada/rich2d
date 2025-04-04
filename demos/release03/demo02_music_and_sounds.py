from rich2d.game import Game, GameConfig
from rich2d.models import ModelGroup, Model
from rich2d.elements import Element
from rich2d.models.ui import Button
from rich2d.audio import Music, Sound

class MusicModel(ModelGroup):
    def __init__(self):
        boccherini_music = Music(file_name="resources/demo02/luigi-boccherini-minuetto.mp3")
        mozart_music = Music(file_name="resources/demo02/wolfgang-amadeus-mozart-fur-elise.mp3")
        fart_sound = Sound(file_name="resources/demo02/fart.mp3")

        class Globals:
            playing_boccherini = False
            playing_mozart = False

        def play_boccherini():
            Globals.playing_boccherini = True
            Globals.playing_mozart = False
            boccherini_music.play()
            return

        def play_mozart():
            Globals.playing_boccherini = False
            Globals.playing_mozart = True
            mozart_music.play()
            return

        def make_fart_sound():
            fart_sound.play()
            return

        def stop_music():
            Globals.playing_boccherini = False
            Globals.playing_mozart = False
            Music.stop_all_music()
            return

        def stop_after_loop():
            Globals.playing_boccherini = False
            Globals.playing_mozart = False
            return

        boccherini_button = Button(rect=(50, 100, 200, 100),
                        text="Play Boccherini",
                        on_left_mouse_click=play_boccherini)

        mozart_button = Button(rect=(550, 100, 200, 100),
                        text="Play Mozart",
                        on_left_mouse_click=play_mozart)

        fart_button = Button(rect=(350, 100, 100, 100),
                        text="Fart",
                        on_left_mouse_click=make_fart_sound)

        stop_button = Button(rect=(150, 250, 200, 100),
                             text="Stop Music",
                             on_left_mouse_click=stop_music)

        stop_after_loop_button = Button(rect=(450, 250, 200, 100),
                                        text="Stop After Loop",
                                        on_left_mouse_click=stop_after_loop)

        def sync_visibility():
            stop_buttons_visible = Music.is_any_music_playing()
            for sprite in stop_button.get_sprites() + stop_after_loop_button.get_sprites():
                sprite.set_visible(stop_buttons_visible)
            return

        def manually_loop():
            if Music.is_any_music_playing():
                pass
            elif Globals.playing_boccherini:
                play_boccherini()
            elif Globals.playing_mozart:
                play_mozart()
            return

        sync_model = Model(elements=[Element(on_update=manually_loop), Element(on_update=sync_visibility)])

        super().__init__(models=[boccherini_button, mozart_button, fart_button,
                                 stop_button, stop_after_loop_button, sync_model])
        return

config = GameConfig(window_title="Music Demo", window_width=800, window_height=600)
game = Game(model=MusicModel(), config=config)
game.run()