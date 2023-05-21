import pygame
from .game_config import GameConfig


class Game:
    def __init__(self, config=None, sprites=[]):
        if config is None:
            config = GameConfig()
        self._config = config
        self._sprites = tuple(sprites)
        return

    def start(self):
        pygame.init()
        config = self._config
        screen = pygame.display.set_mode((config.get_window_width(), config.get_window_height()))
        clock = pygame.time.Clock()
        running = True

        pygame.display.set_caption(config.get_window_title())
        pygame.display.set_icon(config.get_window_icon())

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(config.get_background_colour())
            for sprite in self._sprites:
                sprite.draw(screen)
            pygame.display.flip()
            clock.tick(config.get_frame_rate())

        pygame.quit()
        return

    def get_config(self):
        return self._config

    def get_sprites(self):
        return self._sprites
