import pygame
from os import listdir
from os.path import isfile, join

PLAYER_SPRITE_PATH = "Assets/RedHood"
TILESET_PATH = "Assets/OakWood/oak_woods_tileset.png"

BACKGROUND_IMAGES_NUMBER = 5
BACKGROUND_PATH = "Assets/Background/CityBackgrounds/"

#TODO: Change when levels and mode added 
LEVEL_NUMBER = "1/"
MODE = "Night/"
LEVEL_LENGTH = 10

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_character(width, height, direction=False):
    path = join(PLAYER_SPRITE_PATH)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image))

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0 ,0), rect)
                sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def load_background(width, height):
    bg_images = []

    for i in range(1, BACKGROUND_IMAGES_NUMBER):
        bg_image = pygame.transform.scale(pygame.image.load(BACKGROUND_PATH + LEVEL_NUMBER + MODE + str(i) + ".png"), (width, height))
        bg_images.append(bg_image)

    return bg_images

def parallax_background(window, width, height, offset_x):
    bg_images = load_background(width, height)
    for i in range(LEVEL_LENGTH):
        paralax_speed = 1
        for image in bg_images:
            window.blit(image, (((i * width) - offset_x * paralax_speed), 0))
            paralax_speed += 0.07
