import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()
pygame.display.set_caption("Platformer")

BACKGROUND_LAYER_1 = pygame.transform.scale(pygame.image.load("Assets/Background/background_layer_1.png"), (960, 540))
BACKGROUND_LAYER_2 = pygame.transform.scale(pygame.image.load("Assets/Background/background_layer_2.png"), (960, 540))
BACKGROUND_LAYER_3 = pygame.transform.scale(pygame.image.load("Assets/Background/background_layer_3.png"), (960, 540))
WIDTH, HEIGHT = 960, 540
FPS = 60
PLAYER_VELOCITY = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window):
    window.blit(BACKGROUND_LAYER_1, (0, 0))
    window.blit(BACKGROUND_LAYER_2, (0, 0))
    window.blit(BACKGROUND_LAYER_3, (0, 0))

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

        draw(window)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)