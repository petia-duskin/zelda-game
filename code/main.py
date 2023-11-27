import pygame, sys
from settings import Settings
from debug import debug
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def close(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(Settings.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
