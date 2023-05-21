import pygame
from .game_config import GameConfig


class Game:
    def __init__(self, config=None):
        if config is None:
            config = GameConfig()
        self._config = config
        return

    def start(self):
        pygame.init()
        config = self._config
        screen = pygame.display.set_mode((config.get_window_width(), config.get_window_height()))
        clock = pygame.time.Clock()
        running = True

        pygame.display.set_caption(config.get_window_title())

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(config.get_background_colour())
            pygame.display.flip()
            clock.tick(config.get_frame_rate())

        pygame.quit()
        return

    def get_config(self):
        return self._config
