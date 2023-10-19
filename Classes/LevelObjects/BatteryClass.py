from Classes.LevelObjects.LevelObjectClass import LevelObject, pygame, Sound

IMAGE_PATH = 'Assets/LevelObjects/battery_25x50px.png'

BATTERY_GROUP = pygame.sprite.Group()

class Battery(LevelObject):
    ANIMATION_DELAY = 1
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 18
        self.height = 25
        self.loadSprites(IMAGE_PATH, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 10
        BATTERY_GROUP.add(self)

    def collect(self, player):
        if player.have_gun and player.gun.power < 4:
            player.gun.collectBattery()
            return super().collect()
