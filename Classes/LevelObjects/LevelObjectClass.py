import pygame
from Classes.ObjectClass import Object

class LevelObject(Object):
    ANIMATION_DELAY = 6
    def __init__(self, x, y):
        self.animation_count = 0
        super().__init__(x, y)

    def loadSprites(self, path, factor):
        spritesheet = pygame.image.load(path)
        
        sprites = []
        for i in range(spritesheet.get_width() // self.width):
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * self.width, 0, self.width, self.height)
            surface.blit(spritesheet, (0, 0), rect)
            sprites.append(pygame.transform.scale_by(surface, factor))

        self.sprites = sprites
        self.updateImage()

    def updateImage(self):
        self.image = self.sprites[(self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)]
        self.animation_count += 1

    def draw(self, window, x, y):
        window.blit(self.image, (x, y))
