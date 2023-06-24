import os
import random
import math
import pygame
import sys
sys.path += ["Classes", "Controllers"]

from Classes import Player
from Controllers import PlayerController

pygame.init()
pygame.display.set_caption("Andrei's Crusade")

BACKGROUND_LAYER_1 = pygame.transform.scale(pygame.image.load("Assets/Background/background_layer_1.png"), (960, 540))
BACKGROUND_LAYER_2 = pygame.transform.scale(pygame.image.load("Assets/Background/background_layer_2.png"), (960, 540))
BACKGROUND_LAYER_3 = pygame.transform.scale(pygame.image.load("Assets/Background/background_layer_3.png"), (960, 540))
WIDTH, HEIGHT = 960, 540
FPS = 60
PLAYER_VELOCITY = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


player = Player.Player(100, 100, 50, 50)

def draw(window):
    window.blit(BACKGROUND_LAYER_1, (0, 0))
    window.blit(BACKGROUND_LAYER_2, (0, 0))
    window.blit(BACKGROUND_LAYER_3, (0, 0))

    player.draw(window)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()


    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        player.loop(FPS)
        PlayerController.handle_move(player, keys, PLAYER_VELOCITY)
        draw(window)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)