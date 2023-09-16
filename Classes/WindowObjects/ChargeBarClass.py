import pygame

OBJECT_PATH = 'Assets/MainObjects/bars.png'
WIDTH, HEIGHT = 48, 16

class ChargeBar(pygame.sprite.Sprite):
    def __init__(self, x, y, image_start_y, bar_index, flip=False):
        super().__init__()
        self.flip = flip
        self.bar_index = bar_index
        self.loadSprites(image_start_y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loadSprites(self, image_start_y):
        spriteSheet = pygame.image.load(OBJECT_PATH)
        
        sprites = []
        for i in range(spriteSheet.get_width() // WIDTH):
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * WIDTH, image_start_y, WIDTH, HEIGHT)
            surface.blit(spriteSheet, (0, 0), rect)
            sprites.append(pygame.transform.scale_by(surface, 4))

        self.sprites = sprites
        self.updateImage()

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def decreaseCharge(self):
        if self.bar_index != 4: self.bar_index += 1
        self.updateImage()

    def increaseCharge(self):
        if self.bar_index != 0: self.bar_index -= 1
        self.updateImage()

    def updateImage(self):
        if self.flip: self.image = pygame.transform.flip(self.sprites[self.bar_index], False, True)
        else: self.image = self.sprites[self.bar_index]
