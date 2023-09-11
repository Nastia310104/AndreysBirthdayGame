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
        NOTICE_GROUP.add(self)

    def loadSprites(self):
        spritesheet = pygame.image.load(OBJECT_PATH)
        
        sprites = []
        for i in range(spritesheet.get_width() // WIDTH):
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * WIDTH, 0, WIDTH, HEIGHT)
            surface.blit(spritesheet, (0, 0), rect)
            sprites.append(pygame.transform.scale_by(surface, 2.6))

        self.sprites = sprites
        self.updateImage()

    def updateImage(self):
        self.image = self.sprites[(self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)]
        self.animation_count += 1

    def collect(self, player):
        player.notices += 1        
        return super().collect()
