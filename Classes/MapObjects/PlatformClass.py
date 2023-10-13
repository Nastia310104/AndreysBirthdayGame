from Classes.ObjectClass import Object, pygame, Sound
from Classes.MapObjects.TrapClass import TRAP_GROUP

IMAGE_PATH = 'Assets/MainObjects/Dungeon Tile Set.png'
IMAGE_X, IMAGE_Y = 16, 144
WIDTH, HEIGHT = 48, 6

PLATFORM_GROUP = pygame.sprite.Group()

class Platform(Object):
    def __init__(self, x, y, first_column=True):
        super().__init__(x, y)
        self.loadImage()
        self.start_y = y
        self.rect.x = x
        self.rect.y = y
        self.first_column = first_column
        PLATFORM_GROUP.add(self)
    
    def movePlatform(self):
        for trap in TRAP_GROUP.sprites():
            if self.rect.colliderect(trap.rect):
                self.rect.y += 18
                self.kill()
        if self.rect.y == self.start_y + 222:
            if self.first_column:
                PLATFORM_GROUP.add(Platform(self.rect.x + 180, self.start_y, False))
            else:
                PLATFORM_GROUP.add(Platform(self.rect.x - 180, self.start_y))

        self.rect.y += 3

    def updateImage(self):
        self.movePlatform()
        return super().updateImage()
    
    def loadImage(self):
        spritesheet = pygame.image.load(IMAGE_PATH)
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
        rect = pygame.Rect(IMAGE_X, IMAGE_Y, WIDTH, HEIGHT)
        surface.blit(spritesheet, (0, 0), rect)
        self.image = pygame.transform.scale_by(surface, 2.5)
        self.rect = self.image.get_rect()

