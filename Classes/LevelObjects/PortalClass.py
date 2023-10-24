from Classes.LevelObjects.LevelObjectClass import LevelObject, pygame, Sound

IMAGE_PATH = 'Assets/LevelObjects/Portal_100x100px_line.png'

PORTAL_GROUP = pygame.sprite.Group()

class Portal(LevelObject):
    ANIMATION_DELAY = 2
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 100
        self.height = 100
        self.loadSprites(IMAGE_PATH, 3)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.is_open = False
        PORTAL_GROUP.add(self)

    def draw(self, window, camera):
        if self.is_open:
            self.updateImage()
            return super().draw(window, self.rect.x - camera.offset.x, self.rect.y - camera.offset.y)

    