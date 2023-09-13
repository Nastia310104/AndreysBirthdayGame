from Classes import ObjectClass
import pygame

# TODO: Change for screwdriver icon
IMAGE_PATH = 'Assets/LevelObjects/gun.png'
SCREWDRIVER_GROUP = pygame.sprite.Group()

class Screwdriver(ObjectClass.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(IMAGE_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        