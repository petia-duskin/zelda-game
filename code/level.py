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
        self.visible_sprites = YSortCameraGroup()
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
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)
