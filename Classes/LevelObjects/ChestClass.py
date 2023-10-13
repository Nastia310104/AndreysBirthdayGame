from Classes import ObjectClass
from Classes.LevelObjects.GunClass import Gun, GUN_GROUP
from Classes.LevelObjects.ScrewdriverClass import Screwdriver, SCREWDRIVER_GROUP
from Controllers import SoundsController as Sound
import pygame

OBJECT_PATH = 'Assets/LevelObjects/Object_1.png'
WIDTH, HEIGHT = 32, 32

CHEST_GROUP = pygame.sprite.Group()

class Chest(ObjectClass.Object):
    ANIMATION_DELAY = 6

    def __init__(self, x, y, content):
        super().__init__(x, y)
        self.animation_count = 0
        self.loadSprites()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 2
        self.is_opened = False
        self.content = content
        CHEST_GROUP.add(self)

    def loadSprites(self):
        spriteSheet = pygame.image.load(OBJECT_PATH)
        
        sprites = []
        for i in range(spriteSheet.get_width() // WIDTH):
            surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * WIDTH, 0, WIDTH, HEIGHT)
            surface.blit(spriteSheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        self.sprites = sprites
        self.image = self.sprites[self.animation_count]
    
    def openChest(self):
        index = (self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)
        if index == 3:
            self.is_opened = True
            self.updateContent()
            Sound.CHEST_OPENED.play()

        self.image = self.sprites[index]
        self.animation_count += 1

    def updateContent(self):
        if self.content == "gun":
            self.content = Gun(self.rect.x + 16, self.rect.y - 64)
            GUN_GROUP.add(self.content)
        elif self.content == "screwdriver":
            self.content = Screwdriver(self.rect.x + 16, self.rect.y - 64)
            SCREWDRIVER_GROUP.add(self.content)
