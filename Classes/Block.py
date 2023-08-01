from Classes import Object
from Controllers import SpriteController
import pygame

class Block(Object.Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = SpriteController.load_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

