from Classes import ObjectClass
import pygame

OBJECT_PATH = 'Assets/LevelObjects/Object_3.png'
KEY_GROUP = pygame.sprite.Group()

class Key(ObjectClass.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(OBJECT_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        KEY_GROUP.add(self)

    def collect(self, player):
        player.keys += 1        
        return super().collect()
    
        