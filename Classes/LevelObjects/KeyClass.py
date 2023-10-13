import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject
from Controllers import SoundsController as Sound

IMAGE_PATH = 'Assets/LevelObjects/key.png'

KEY_GROUP = pygame.sprite.Group()

class Key(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 16
        self.height = 16
        self.loadSprites(IMAGE_PATH, 3)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        KEY_GROUP.add(self)

    def collect(self, player):
        player.keys.append(self)
        Sound.GEAR_OR_KEY_COLLECTED.play()
        return super().collect()
    