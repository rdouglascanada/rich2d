import pygame
from .game_config import GameConfig
from models import Model


class Game:
    def __init__(self, config=None, model=None):
        if config is None:
            config = GameConfig()
        if model is None:
            model = Model()
        self._config = config
        self._model = model
        return

    def run(self):
        pygame.init()
        config = self._config
        model = self._model
        screen = pygame.display.set_mode((config.get_window_width(), config.get_window_height()))
        clock = pygame.time.Clock()
        running = True

        pygame.display.set_caption(config.get_window_title())
        pygame.display.set_icon(config.get_window_icon())

        while running:
            for event in pygame.event.get():
                for handler in model.get_handlers():
                    handler.handle_event(event)
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(config.get_background_colour())
            for element in model.get_elements():
                element.update()
            for sprite in model.get_sprites():
                sprite.draw(screen)
            pygame.display.flip()
            clock.tick(config.get_frame_rate())

        pygame.quit()
        return
