import pygame
from Classes import ObjectClass

OBJECT_PATH = 'Assets/LevelObjects/Object_4.png'

ENEMY_GROUP = pygame.sprite.Group()

class Enemy(ObjectClass.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(OBJECT_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        ENEMY_GROUP.add(self)
