from Classes.LevelObjects.LevelObjectClass import LevelObject, pygame, Sound

IMAGE_PATH = 'Assets/LevelObjects/Entry.png'

DOOR_GROUP = pygame.sprite.Group()

class Door(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 32
        self.height = 64
        self.loadSprites(IMAGE_PATH, 2)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_opened = False
        DOOR_GROUP.add(self)

    def openDoor(self, player):
        index = (self.animation_count // self.ANIMATION_DELAY) % 4
        if index == 3:
            Sound.DOOR_OPENS.play()
            self.is_opened = True
            player.keys.pop(len(player.keys) - 1)

        self.image = self.sprites[index]
        self.animation_count += 1

    def checkKey(self, player):
        if len(player.keys) > 0:
            self.openDoor(player)

    def updateImage(self):
        return