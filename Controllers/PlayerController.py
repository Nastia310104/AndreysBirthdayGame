from Classes import Player
import pygame

def handle_move(Player, keys, velocity):
    Player.x_vel = 0

    if keys[pygame.K_LEFT]:
        Player.move_left(velocity)
    elif keys[pygame.K_RIGHT]:
        Player.move_right(velocity)

