from Classes.ObjectClass import Object, pygame

IMAGE_PATH = 'Assets/LevelObjects/bullet.png'
BULLET_GROUP = pygame.sprite.Group()

class Bullet(Object):
    SPEED = 15
    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.image = pygame.transform.scale2x(pygame.image.load(IMAGE_PATH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.lifetime = 60
        BULLET_GROUP.add(self)

    def loop(self, tiles):
        if self.lifetime > 0:
            self.updatePosition()
            self.checkCollisionX(tiles)
            self.lifetime -= 1
        else:
            self.kill()
        
    def updatePosition(self):
        if self.direction == 'right':
            self.rect.x += self.SPEED
        elif self.direction == 'left':
            self.rect.x -= self.SPEED

    def checkCollisionX(self, tiles):
        for tile in tiles:
            if self.rect.colliderect(tile):
                self.kill()

    def draw(self, window, camera):
        window.blit(self.image, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))

