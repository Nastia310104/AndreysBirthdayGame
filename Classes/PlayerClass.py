import pygame
import Controllers.SpriteController as Sprite, Controllers.SoundsController as Sound, Controllers.MenuController as Menu
from Classes.LevelObjects.ChestClass import Chest
from Classes.LevelObjects.GunClass import GUN_GROUP
from Classes.LevelObjects.ScrewdriverClass import SCREWDRIVER_GROUP
from Classes.WindowObjects.ChargeBarClass import ChargeBar
from Classes.EnemyClass import Enemy
from Classes.MapObjects.BlockClass import Block
from Classes.LevelObjects.DoorClass import Door
from Classes.MapObjects.TrapClass import Trap
from Classes.MapObjects.PlatformClass import Platform, PLATFORM_GROUP
from Classes.LevelObjects.OfficeClass import Table
from Classes.LevelObjects.PortalClass import Portal

PLAYER_SPRITE_PATH = "Assets/RedHood"

class Player(pygame.sprite.Sprite):
    CHARACTER_WIDTH, CHARACTER_HEIGHT = 32, 32
    SPRITES = Sprite.loadSprites(PLAYER_SPRITE_PATH, CHARACTER_WIDTH, CHARACTER_HEIGHT, True)
    START_POSITION_X, START_POSITION_Y = 200, 800
    ANIMATION_DELAY = 4

    # TODO:Mask collision

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
# Player's statments
        self.have_gun = False
        self.have_screwdriver = False
        self.go_left, self.go_right = False, False
        self.is_jumping, self.on_ground = False, False
        self.is_dead = False
        self.is_dieing = False
        self.is_attack = False
        self.level_complete = False
        self.in_portal = False
        self.tools_collected = False
# Player's counters
        self.jump_count = 0
        self.injured_time_count = 0
        self.animation_count = 0
        self.attack_count = 0
        self.health = 4
        self.notices = []
        self.gears = []
        self.keys = []
# Player's position
        self.rect = pygame.Rect(self.START_POSITION_X, self.START_POSITION_Y, self.CHARACTER_WIDTH * 2, self.CHARACTER_HEIGHT * 2)
        self.position = pygame.math.Vector2(self.START_POSITION_X, self.START_POSITION_Y)
        self.velocity = pygame.math.Vector2(0,0)
        self.gravity, self.friction = .35, -.12
        self.acceleration = pygame.math.Vector2(0,self.gravity)
# Player's properties
        self.direction = "right"
        self.health_bar = ChargeBar(200, 50, 80, 0, True)
    
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
        self.checkHealth()
        self.move(dt, tiles)
        self.handleAttack()
        self.updateSprite()

    def checkHealth(self):
        if self.health == 0 and not self.is_dieing:
            Sound.PLAYER_DEAD.play()
            self.is_dieing = True
            self.animation_count = 0
            self.dieing_count = 0
            self.go_left = False
            self.go_right = False
        elif self.is_dieing and self.animation_count >= 42:
            self.animation_count = 42
            self.is_dead = True

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
        Sound.JUMP.play()
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
        tiles += (GUN_GROUP.sprites() + SCREWDRIVER_GROUP.sprites() + PLATFORM_GROUP.sprites())
        for tile in tiles:
            if self.rect.colliderect(tile):
                if isinstance(tile, Chest):
                    if not tile.is_opened:
                        tile.openChest()
                elif isinstance(tile, Door):
                    if not tile.is_opened:
                        hits.append(tile)
                        tile.checkKey(self)
                elif isinstance(tile, Block) or isinstance(tile, Platform):
                    hits.append(tile)
                elif isinstance(tile, Table):
                    tile.checkParts(self)
                elif isinstance(tile, Portal):
                    if self.tools_collected:
                        tile.is_open = True
                        self.level_complete = True
                elif isinstance (tile, Trap):
                    self.health = 0
                    hits.append(tile)
                elif isinstance (tile, Enemy):
                    if not tile.is_dead and not self.is_dieing:
                        if self.injured_time_count <= 0:
                            self.injured_time_count = 30
                            self.health_bar.decreaseCharge()
                            self.health -= 1
                            Sound.PLAYER_HURT.play()
                        self.injured_time_count -= 1
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
                if isinstance(tile, Platform):
                    self.position.y += 3
                self.rect.bottom = self.position.y
            elif self.velocity.y < 0:
                self.velocity.y = 0
                self.position.y = tile.rect.bottom + self.rect.h
                if isinstance(tile, Platform):
                    self.position.y += 6
                self.rect.bottom = self.position.y

########################### Animate character ###########################

    def updateSprite(self):
        self.ANIMATION_DELAY = 4
        if self.is_dieing:
            self.spritesheet = "die"
            self.ANIMATION_DELAY = 6
        elif self.in_portal:
            self.spritesheet = "disappear"
            self.ANIMATION_DELAY = 6
        elif self.is_attack:
            self.spritesheet = "attack"
        elif self.velocity.y < 0:
            if self.jump_count <= 2:
                self.spritesheet = "jump"
        elif self.velocity.y > self.gravity * 2:
            self.spritesheet = "fall"
        elif self.go_left or self.go_right:
            self.spritesheet = "run"
        else:
            self.spritesheet = "idle"
            self.ANIMATION_DELAY = 8
            
        spritesheet_name = self.spritesheet + "_" + self.direction
        sprites = self.SPRITES[spritesheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
