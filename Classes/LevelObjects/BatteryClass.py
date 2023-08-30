from Classes import ObjectClass
import pygame

class Battery(ObjectClass.Object):
    def __init__(self, image, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        