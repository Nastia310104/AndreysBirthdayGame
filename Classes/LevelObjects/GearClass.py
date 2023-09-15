import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject

IMAGE_PATH = 'Assets/LevelObjects/Object_2.png'

GEAR_GROUP = pygame.sprite.Group()

class Gear(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 16
        self.height = 16
        self.loadSprites(IMAGE_PATH, 3)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        GEAR_GROUP.add(self)

    def collect(self, player):
        player.gears.append(self)    
        return super().collect()
