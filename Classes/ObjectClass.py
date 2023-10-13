import pygame
import Controllers.SoundsController as Sound

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width=64, height=64, name=None):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)
        self.wigth = width
        self.height = height
        self.name = name
        self.is_collected = False

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collect(self):
        self.is_collected = True
        self.kill()

    def updateImage(self):
        return
