from Classes import Player
import pygame

def handle_move(player, keys, velocity, objects):
    player.x_vel = 0

    if keys[pygame.K_LEFT]:
        player.move_left(velocity)
    elif keys[pygame.K_RIGHT]:
        player.move_right(velocity)

    handle_vertical_collision(player, objects, player.y_vel)

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for object in objects:
        if pygame.sprite.collide_mask(player, object):
            if dy > 0:
                player.rect.bottom = object.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = object.rect.bottom
                player.hit_head()

        collided_objects.append(object)
    return collided_objects

