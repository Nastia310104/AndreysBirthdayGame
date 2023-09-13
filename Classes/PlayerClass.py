import pygame
import Controllers.SpriteController as Sprite
from Classes.LevelObjects.ChestClass import Chest
from Classes.EnemyClass import Enemy
from Classes.BlockClass import Block
from Classes.ChargeBarClass import ChargeBar
from Classes.LevelObjects.GunClass import GUN_GROUP

PLAYER_SPRITE_PATH = "Assets/RedHood"

class Player(pygame.sprite.Sprite):
    CHARACTER_WIDTH, CHARACTER_HEIGHT = 32, 32
    SPRITES = Sprite.loadSprites(PLAYER_SPRITE_PATH, CHARACTER_WIDTH, CHARACTER_HEIGHT, True)
    START_POSITION_X, START_POSITION_Y = 200, 800
    ANIMATION_DELAY = 4

    # TODO:Mask collision

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.go_left, self.go_right = False, False
        self.is_jumping, self.on_ground = False, False
        self.is_dead = False
        self.is_attack = False
        self.gravity, self.friction = .35, -.12
        self.position = pygame.math.Vector2(self.START_POSITION_X, self.START_POSITION_Y)
        self.velocity = pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,self.gravity)
        self.jump_count = 0
        self.animation_count = 0
        self.attack_count = 0
        self.rect = pygame.Rect(self.START_POSITION_X, self.START_POSITION_Y, self.CHARACTER_WIDTH * 2, self.CHARACTER_HEIGHT * 2)
        self.direction = "right"

        self.health = 100
        self.notices = 0
        self.gears = 0
        self.keys = 0
        self.have_gun = False
        self.have_screwdriver = False
        self.health_bar = ChargeBar(200, 50, 80, 0)
    
    def draw(self, window, camera):
        window.blit(self.sprite, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))
        self.health_bar.draw(window)
        if self.have_gun:
            self.gun.draw(window)
            self.gun.power_bar.draw(window)

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))

        if abs(self.velocity.x) < .01:
            self.velocity.x = 0

    def loop(self, dt, tiles):
        self.move(dt, tiles)
        self.handleAttack()
        self.update_sprite()

########################### Handle movement ###########################

    def move(self, dt, tiles):
        self.horizontal_movement(dt)
        self.checkCollisionsx(tiles)
        self.vertical_movement(dt)
        self.checkCollisionsy(tiles)

    def horizontal_movement(self, dt):
        self.acceleration.x = 0
        if self.go_left:
            self.acceleration.x -= .3
            self.direction = "left"
        elif self.go_right:
            self.acceleration.x += .3
            self.direction = "right"
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(5)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

    def vertical_movement(self, dt):
        self.velocity.y += self.acceleration.y * dt

        if self.velocity.y > 7:
            self.velocity.y = 7

        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y

########################### Handle jumping ###########################

    def jump(self):
        self.animation_count = 0
        if self.jump_count == 1:
            self.velocity.y -= 5 * self.gravity
        self.is_jumping = True
        self.velocity.y -= 10
        self.on_ground = False
        self.jump_count += 1

########################### Handle attack ###########################
    def handleAttack(self):
        if self.is_attack == True:
            if self.attack_count >= 30:
                self.is_attack = False
                self.attack_count = 0
            elif self.attack_count < 30:
                self.attack_count += 1

    def attack(self):
        if self.have_gun == True and self.gun.power > 0 and self.gun.cooldown == 0:
            self.is_attack = True
            self.animation_count = 0
            self.gun.shoot(self)

########################### Check collision ###########################

    def get_hits(self, tiles):
        hits = []
        if len(GUN_GROUP.sprites()) > 0:
            tiles += GUN_GROUP.sprites()
        for tile in tiles:
            if self.rect.colliderect(tile):
                if isinstance(tile, Chest):
                    if not tile.is_opened:
                        tile.openChest()
                elif isinstance(tile, Block):
                    hits.append(tile)
                elif isinstance (tile, Enemy) and not tile.is_dead:
                    self.health_bar.decreaseCharge()
                else:
                    self.collectObject(tile)

        return hits
    
    def collectObject(self, object):
        if not object.is_collected:
            object.collect(self)

    def checkCollisionsx(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.x > 0:
                self.position.x = tile.rect.left - self.rect.w
                self.rect.x = self.position.x
            elif self.velocity.x < 0:
                self.position.x = tile.rect.right
                self.rect.x = self.position.x

    def checkCollisionsy(self, tiles):
        self.on_ground = False
        self.rect.bottom += 1
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.y > 0:
                self.on_ground = True
                self.jump_count = 0
                self.is_jumping = False
                self.velocity.y = 0
                self.position.y = tile.rect.top
                self.rect.bottom = self.position.y
            elif self.velocity.y < 0:
                self.velocity.y = 0
                self.position.y = tile.rect.bottom + self.rect.h
                self.rect.bottom = self.position.y

########################### Animate character ###########################

    def update_sprite(self):
        self.spritesheet = "idle"
        if self.is_attack:
            self.spritesheet = "attack"
        elif self.velocity.y < 0:
            if self.jump_count <= 2:
                self.spritesheet = "jump"
        elif self.velocity.y > self.gravity * 2:
            self.spritesheet = "fall"
        elif self.go_left or self.go_right:
            self.spritesheet = "run"
            
        spritesheet_name = self.spritesheet + "_" + self.direction
        sprites = self.SPRITES[spritesheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
