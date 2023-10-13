from Classes.ObjectClass import Object, pygame

TRAP_GROUP = pygame.sprite.Group()

IMAGE_PATH = 'Assets/Tiles/Tile_65.png'

class Trap(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(IMAGE_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        TRAP_GROUP.add(self)
        