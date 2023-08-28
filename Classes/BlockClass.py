from Classes import ObjectClass
from Controllers import SpriteController
import pygame

class Block(ObjectClass.Object):
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale2x(pygame.image.load(image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    # def draw(self, window):
    #     window.blit(self.image, (self.rect.x, self.rect.y))
