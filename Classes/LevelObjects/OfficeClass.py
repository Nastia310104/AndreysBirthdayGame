from Classes.LevelObjects.LevelObjectClass import LevelObject, pygame, Sound

TABLE_IMAGE_PATH = 'Assets/LevelObjects/Table.png'
CHAIR_IMAGE_PATH = 'Assets/LevelObjects/Chair.png'

OFFICE_GROUP = pygame.sprite.Group()

class Table(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 49
        self.height = 16
        self.image = pygame.transform.scale2x(pygame.image.load(TABLE_IMAGE_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 32
        OFFICE_GROUP.add(self)

    def checkParts(self, player):
        if len(player.notices) == 3 and player.have_screwdriver:
            player.tools_collected = True

class Chair(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 20
        self.height = 24
        self.image = pygame.transform.scale2x(pygame.image.load(CHAIR_IMAGE_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x + 32
        self.rect.y = y + 16
        OFFICE_GROUP.add(self)
