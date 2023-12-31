from Classes.LevelObjects.LevelObjectClass import LevelObject, pygame, Sound

IMAGE_PATH = 'Assets/LevelObjects/screwdriver.png'

SCREWDRIVER_GROUP = pygame.sprite.Group()

class Screwdriver(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 32
        self.height = 32
        self.loadSprites(IMAGE_PATH, 1.5)
        self.portrait_image = pygame.transform.rotate(pygame.transform.scale2x(self.image), 135)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collect(self, player):
        Sound.TOOLS_COLLECTED.play()
        player.screwdriver = self
        player.have_screwdriver = True
        return super().collect()
    