from Classes import ObjectClass
from Classes.WindowObjects.ChargeBarClass import ChargeBar
from Classes.LevelObjects.BulletClass import Bullet, BULLET_GROUP

import pygame

IMAGE_PATH = 'Assets/LevelObjects/gun.png'
GUN_GROUP = pygame.sprite.Group()

class Gun(ObjectClass.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(IMAGE_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collected = False
        self.power = 1
        self.cooldown = 0
        self.power_bar = ChargeBar(200, 78, 16, 3)

    def collect(self, player):
        player.gun = self
        player.have_gun = True
        return super().collect()
    
    def draw(self, window):
        if self.cooldown > 0: self.cooldown -= 1
        window.blit(pygame.transform.scale_by(self.image, 1.8), (375, 98))

    def collectBattery(self):
        self.power_bar.increaseCharge()
        self.power += 1

    def shoot(self, player):
        if player.direction == 'right':
            Bullet(player.rect.x + player.rect.width, player.rect.y + (player.rect.height // 2), player.direction)
        else:
            Bullet(player.rect.x, player.rect.y + (player.rect.height // 2), player.direction)
        self.power -= 1
        self.power_bar.decreaseCharge()
        self.cooldown = 30
