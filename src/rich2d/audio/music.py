from pygame.mixer import init, music as pygame_music

class Music:
    _pygame_mixer_initialized = False
    _last_loaded_file = None

    def __init__(self, file_name=None):
        if file_name is None:
            raise RuntimeError("Music file_name cannot be None")
        self._file_name = file_name
        if not Music._pygame_mixer_initialized:
            init()
        return

    def play(self, loops=0):
        if Music._last_loaded_file is not None:
            pygame_music.unload()
            Music._last_loaded_file = None
        pygame_music.load(self._file_name)
        Music._last_loaded_file = self._last_loaded_file
        pygame_music.play(loops=loops)
        return

    def play_indefinitely(self):
        self.play(loops=-1)
        return

    def stop(self):
        Music.stop_all_music()
        if Music._last_loaded_file is not None:
            pygame_music.unload()
            Music._last_loaded_file = None
        return

    def is_playing(self):
        return (Music._last_loaded_file is not None) and (self._file_name == Music._last_loaded_file) \
                and pygame_music.get_busy()

    @staticmethod
    def is_any_music_playing():
        return pygame_music.get_busy()

    @staticmethod
    def stop_all_music():
        pygame_music.stop()
        if Music._last_loaded_file:
            pygame_music.unload()
        return

