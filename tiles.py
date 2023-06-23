import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super(Tile, self).__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super(Coin, self).__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((212, 175, 55))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift