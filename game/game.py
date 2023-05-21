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

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(config.get_background_colour())
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        return