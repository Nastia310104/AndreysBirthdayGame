import pygame
from abc import abstractmethod, ABC


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width=64, height=64, name=None):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)
        self.wigth = width
        self.height = height
        self.name = name

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
