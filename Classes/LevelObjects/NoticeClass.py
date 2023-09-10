from Classes import ObjectClass
import pygame

OBJECT_PATH = 'Assets/LevelObjects/Object_0.png'
WIDTH, HEIGHT = 24, 24

NOTICE_GROUP = pygame.sprite.Group()

class Notice(ObjectClass.Object):
    ANIMATION_DELAY = 6

    def __init__(self, x, y):
        super().__init__(x, y)
        self.animation_count = 0
        self.loadSprites()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collected = False
        NOTICE_GROUP.add(self)

    def loadSprites(self):
        spriteSheet = pygame.image.load(OBJECT_PATH)
        
        sprites = []
        for i in range(spriteSheet.get_width() // WIDTH):
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * WIDTH, 0, WIDTH, HEIGHT)
            surface.blit(spriteSheet, (0, 0), rect)
            sprites.append(pygame.transform.scale_by(surface, 2.6))

        self.sprites = sprites
        self.update_image()

    def collect(self):
        self.is_collected = True
        self.kill()

    def update_image(self):
        self.image = self.sprites[(self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)]
        self.animation_count += 1
