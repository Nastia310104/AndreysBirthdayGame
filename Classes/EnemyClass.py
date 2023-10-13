import pygame
from Classes.ObjectClass import Object
import Controllers.SpriteController as Sprite, Controllers.SoundsController as Sound
from Classes.LevelObjects.BulletClass import Bullet, BULLET_GROUP

ENEMY_SPRITE_PATH = 'Assets/NPSs/Slime/'

ENEMY_GROUP = pygame.sprite.Group()

class Enemy(Object):
    ANIMATION_DELAY = 4
    VELOCITY = 4
    VISION_LENGTH = 192
    WIDTH, HEIGHT = 32, 24

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprites = Sprite.loadSprites(ENEMY_SPRITE_PATH, self.WIDTH, self.HEIGHT, False, True)
        self.rect = pygame.Rect(x, y + 16, self.WIDTH * 2, self.HEIGHT * 2)
        self.vision = pygame.Rect(x - self.VISION_LENGTH, (y + 16 - self.VISION_LENGTH), self.VISION_LENGTH, self.HEIGHT * 2)
# Enemy's conditions
        self.direction = "right"
        self.is_attack = False
        self.is_dead = False
# Enemy's counters
        self.dieing_count = 0
        self.animation_count = 0
        self.attack_counter = 0
        ENEMY_GROUP.add(self)

    def loop(self, tiles, player):
        if self.is_dead == False:
            self.move(tiles)
            self.checkPlayerCollision(player)
            self.checkBulletCollision()
            self.updateImage()
        else:
            self.die()

    def die(self):
        if self.dieing_count == 30:
            self.kill()
        elif self.dieing_count == 10:
            Sound.ENEMY_DIE.play()
        self.image = self.sprites['blow_' + self.direction][(self.dieing_count // int(self.ANIMATION_DELAY * 1.5)) % 5]
        self.dieing_count += 1

########################### Handle movement ###########################

    def move(self, tiles):
        self.handleMovement()
        self.checkCollisionsx(tiles)

    def handleMovement(self):
        if self.direction == "right":
            self.velocity_x = self.VELOCITY
            self.rect.x += self.velocity_x
            self.vision.x = self.rect.x + 64
            self.vision.y = self.rect.y
        elif self.direction == "left":
            self.velocity_x = -self.VELOCITY
            self.rect.x += self.velocity_x
            self.vision.x = self.rect.x - self.VISION_LENGTH
            self.vision.y = self.rect.y

    def moveLeft(self):
        self.direction = "left"
        self.animation_count = 0

    def moveRight(self):
        self.direction = "right"
        self.animation_count = 0

########################### Check collisions ###########################

    def getHits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    def checkCollisionsx(self, tiles):
        collisions = self.getHits(tiles)
        for tile in collisions:
            if self.velocity_x > 0:
                self.direction = "left"
            elif self.velocity_x < 0:
                self.direction = "right"

    def checkPlayerCollision(self, player):
        if self.vision.colliderect(player) and not player.is_dead:
            if self.is_attack == False:
                Sound.ENEMY_ATTACK.play()
                self.animation_count = 0
                self.is_attack = True
                self.VELOCITY = 10
        elif self.attack_counter <= 0:
            self.attack_counter = 30
            self.is_attack = False
            self.VELOCITY = 4
    
    def checkBulletCollision(self):
        for bullet in BULLET_GROUP.sprites():
            if self.rect.colliderect(bullet):
                Sound.ENEMY_HURT.play()
                self.is_dead = True
                bullet.kill()

########################### Draw enemy ###########################

    def updateImage(self):
        if self.is_attack == True:
            self.spritesheet = 'attack'
        else:
            self.spritesheet = 'walk'

        spritesheet_name = self.spritesheet + "_" + self.direction
        sprites = self.sprites[spritesheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.attack_counter -= 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

    def draw(self, window, camera):
        window.blit(self.image, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))
