import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject
from Controllers import SoundsController as Sound

IMAGE_PATH = 'Assets/LevelObjects/gear.png'

GEAR_GROUP = pygame.sprite.Group()

class Gear(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 32
        self.height = 32
        self.loadSprites(IMAGE_PATH, 1.5)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        GEAR_GROUP.add(self)

    def collect(self, player):
        Sound.GEAR_OR_KEY_COLLECTED.play()
        player.gears.append(self)    
        return super().collect()
