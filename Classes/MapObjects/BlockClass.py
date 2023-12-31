from Classes.ObjectClass import Object, pygame

BLOCK_GROUP = pygame.sprite.Group()

class Block(Object):
    def __init__(self, image, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        BLOCK_GROUP.add(self)
        