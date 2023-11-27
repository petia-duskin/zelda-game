import pygame
from settings import Settings
from tile import Tile
from player import Player
from debug import debug


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(Settings.WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * Settings.TILESIZE
                y = row_index * Settings.TILESIZE
                if column == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if column == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
