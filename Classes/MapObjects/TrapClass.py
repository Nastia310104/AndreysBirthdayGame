from Classes.LevelObjects.LevelObjectClass import LevelObject, pygame

TRAP_GROUP = pygame.sprite.Group()

IMAGE_PATH = 'Assets/MainObjects/lightning.png'

class Trap(LevelObject):
    ANIMATION_DELAY = 4
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 32
        self.height = 96
        self.loadSprites(IMAGE_PATH, 4)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 16
        TRAP_GROUP.add(self)

    def updateImage(self):
        super().updateImage()
        self.image = pygame.transform.rotate(self.image, 90)
        