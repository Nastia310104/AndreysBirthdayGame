import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject

IMAGE_PATH = 'Assets/MainObjects/heart.png'

HEART_GROUP = pygame.sprite.Group()

class Heart(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.animation_count = 0
        self.width = 16
        self.height = 16
        self.loadSprites(IMAGE_PATH, 3)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        HEART_GROUP.add(self)

    def collect(self, player):
        if player.health < 4:
            player.health += 1
            player.health_bar.increaseCharge()
        return super().collect()
    