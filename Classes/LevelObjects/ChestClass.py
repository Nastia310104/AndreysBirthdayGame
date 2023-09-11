from Classes import ObjectClass
import pygame

OBJECT_PATH = 'Assets/LevelObjects/Object_1.png'
WIDTH, HEIGHT = 32, 32

CHEST_GROUP = pygame.sprite.Group()

class Chest(ObjectClass.Object):
    ANIMATION_DELAY = 6

    def __init__(self, x, y):
        super().__init__(x, y)
        self.animation_count = 0
        self.loadSprites()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 2
        self.is_opened = False
        CHEST_GROUP.add(self)

    def loadSprites(self):
        spriteSheet = pygame.image.load(OBJECT_PATH)
        
        sprites = []
        for i in range(spriteSheet.get_width() // WIDTH):
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * WIDTH, 0, WIDTH, HEIGHT)
            surface.blit(spriteSheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        self.sprites = sprites
        self.image = self.sprites[self.animation_count]
    
    def openChest(self):
        index = (self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)
        if index == 3:
            self.is_opened = True

        self.image = self.sprites[index]
        self.animation_count += 1
