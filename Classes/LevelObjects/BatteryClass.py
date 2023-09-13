from Classes import ObjectClass
import pygame

IMAGE_PATH = 'Assets/LevelObjects/Battery/battery_'
BATTERY_GROUP = pygame.sprite.Group()

class Battery(ObjectClass.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.animation_count = 1
        self.update()
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 10
        BATTERY_GROUP.add(self)

    def updateImage(self):
        if self.animation_count == 61: self.animation_count = 1

        self.image = pygame.transform.scale_by((pygame.image.load(IMAGE_PATH + str(self.animation_count) + '.png')), 2)
        self.animation_count += 1

    def collect(self, player):
        if player.have_gun:
            player.gun.collectBattery()
        return super().collect()
