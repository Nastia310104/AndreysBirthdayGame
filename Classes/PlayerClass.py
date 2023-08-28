import pygame
import Controllers.SpriteController as Sprite

class Player(pygame.sprite.Sprite):
    CHARACTER_WIDTH, CHARACTER_HEIGHT = 32, 32
    SPRITES = Sprite.load_character(CHARACTER_WIDTH, CHARACTER_HEIGHT, True)
    START_POSITION_X, START_POSITION_Y = 200, 800
    ANIMATION_DELAY = 8

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.go_left, self.go_right = False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .35, -.12
        self.position, self.velocity = pygame.math.Vector2(self.START_POSITION_X, self.START_POSITION_Y), pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,self.gravity)
        self.jump_count = 0
        self.animation_count = 0
        self.rect = pygame.Rect(self.START_POSITION_X, self.START_POSITION_Y, self.CHARACTER_WIDTH, self.CHARACTER_HEIGHT)
        self.direction = "right"
        self.ground_y = 500

    def draw(self, window, camera):
        window.blit(self.sprite, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))

    def move(self, dt, tiles):
        self.horizontal_movement(dt)
        self.checkCollisionsx(tiles)
        self.vertical_movement(dt)
        self.checkCollisionsy(tiles)

    def horizontal_movement(self,dt):
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

    def vertical_movement(self,dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        self.animation_count = 0
        if self.jump_count == 1:
            self.velocity.y -= 5 * self.gravity
        self.is_jumping = True
        self.velocity.y -= 10
        self.on_ground = False
        self.jump_count += 1

    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)

        return hits

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

    def loop(self, dt, tiles):
        self.move(dt, tiles)
        self.update_sprite()

    def update_sprite(self):
        self.spritesheet = "idle"
        if self.velocity.y < 0:
            if self.jump_count <= 2:
                self.spritesheet = "jump"
        elif self.velocity.y > self.gravity * 2:
            self.spritesheet = "fall"
        elif self.go_left or self.go_right:
            self.spritesheet = "run"

        sprite_sheet_name = self.spritesheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
