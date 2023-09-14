import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject

IMAGE_PATH = 'Assets/LevelObjects/sabstitude.png'

GEAR_GROUP = pygame.sprite.Group()

class MainObject(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 16
        self.height = 16
        self.loadSprites(IMAGE_PATH, 6)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        GEAR_GROUP.add(self)
