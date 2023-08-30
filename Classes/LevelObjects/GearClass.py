from Classes import ObjectClass
import pygame

GEAR_GROUP = pygame.sprite.Group()

class Gear(ObjectClass.Object):
    def __init__(self, x, y, window):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load("Assets/MainObjects/Object_2.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collected = False
        self.window = window
        GEAR_GROUP.add(self)

    def collectGear(self):
        self.is_collected = True
        print(self.groups())
        self.kill()
        print(self.groups)
        GEAR_GROUP.draw(self.window)