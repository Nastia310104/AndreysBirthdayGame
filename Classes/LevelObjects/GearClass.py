from Classes import ObjectClass
from Controllers import SpriteController
import pygame

GEAR_GROUP = pygame.sprite.Group()

class Gear(ObjectClass.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load("Assets/MainObjects/Object_2.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collected = False
        GEAR_GROUP.add(self)
        self.position_x = x
        self.position_y = y

    def collectGear(self):
        self.is_collected = True
        self.kill()

    def update(self, x, y):
        print(self.position_y)
        self.rect.x += x
        # self.rect.y = self.position_y - y + self.rect.height
        print(self.position_y)
