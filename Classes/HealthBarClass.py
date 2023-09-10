import pygame

OBJECT_PATH = 'Assets/MainObjects/HealthBar.png'
WIDTH, HEIGHT = 48, 16

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bar_index = 0
        self.loadSprites()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loadSprites(self):
        spriteSheet = pygame.image.load(OBJECT_PATH)
        
        sprites = []
        for i in range(spriteSheet.get_width() // WIDTH):
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * WIDTH, 80, WIDTH, HEIGHT)
            surface.blit(spriteSheet, (0, 0), rect)
            sprites.append(pygame.transform.scale_by(surface, 4))

        self.sprites = sprites
        self.image = self.sprites[self.bar_index]

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def decreaseHealth(self):
        if self.bar_index != 4: self.bar_index += 1
        self.image = self.sprites[self.bar_index]
