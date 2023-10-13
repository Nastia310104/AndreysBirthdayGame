import pygame

BACKGROUND_IMAGES_PATH = "Assets/Background/CityBackgrounds/"
BACKGROUND_IMAGES_NUMBER = 5
#TODO: Change when levels and mode added 
# TODO: Change slime=False when enemy added
LEVEL_NUMBER = "1/"
MODE = "Night/"
LEVEL_LENGTH = 10

class Background():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.images = self.load_background(width, height)

    def load_background(self, width, height):
        bg_images = []
        for i in range(1, BACKGROUND_IMAGES_NUMBER):
            bg_image = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGES_PATH + LEVEL_NUMBER + MODE + str(i) + ".png"), (width, height))
            bg_images.append(bg_image)

        return bg_images

    def parallax_background(self, window, offset_x):
        for i in range(LEVEL_LENGTH):
            paralax_speed = 1
            for image in self.images:
                window.blit(image, (((i * self.width) - offset_x * paralax_speed), 0))
                paralax_speed += 0.07
