import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject
from Controllers import SoundsController as Sound

IMAGE_PATH = 'Assets/LevelObjects/Object_0.png'

NOTICE_GROUP = pygame.sprite.Group()

class Notice(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 24
        self.height = 24
        self.loadSprites(IMAGE_PATH, 2.6)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        NOTICE_GROUP.add(self)

    def collect(self, player):
        Sound.NOTICE_COLLECTED.play()
        player.notices.append(self)       
        return super().collect()
