import pygame
from Classes.LevelObjects.HeartClass import Heart, HEART_GROUP
from Classes.MainDeviceClass import MainObject

FRAME_PATH = 'Assets/MainObjects/GUI.png'

MAIN_FRAIM_X, MAIN_FRAIM_Y, MAIN_FRAIM_W, MAIN_FRAIM_H = 80, 96, 32 ,32
NAME_FRAIM_X, NAME_FRAIM_Y, NAME_FRAIM_W, NAME_FRAIM_H = 144, 96, 64, 16

FONT = pygame.font.SysFont('Cybersomething', 30)
NAME = 'Andrei'

class Portrait():
    def __init__(self, x, y):
        super().__init__()
        self.main_fraim = self.loadSprites(MAIN_FRAIM_X, MAIN_FRAIM_Y, MAIN_FRAIM_W, MAIN_FRAIM_H)
        self.name_fraim = self.loadSprites(NAME_FRAIM_X, NAME_FRAIM_Y, NAME_FRAIM_W, NAME_FRAIM_H)
        self.char_name = self.createTextImage(NAME, (229, 228, 226))
        self.main_object = MainObject(0 ,0)
        self.rect = self.main_fraim.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.heart = Heart(375, 50)
        HEART_GROUP.remove(self.heart)
        self.getPositions()

    def loadSprites(self, x, y, width, height):
        spritesheet = pygame.image.load(FRAME_PATH)
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(x, y, width, height)
        surface.blit(spritesheet, (0, 0), rect)

        return pygame.transform.scale_by(surface, 4)
    
    def createTextImage(self, text, color):
        return FONT.render(text, True, color)
    
    def getPositions(self):
        self.name_fraim_position = pygame.math.Vector2(self.rect.x + self.main_fraim.get_width(), self.rect.y)
        self.char_name_position = pygame.math.Vector2(self.name_fraim_position.x + ((self.name_fraim.get_width() - self.char_name.get_width()) // 3.8), (self.rect.y + (self.name_fraim.get_height() - self.char_name.get_height()) // 2))

    def draw(self, window, player):
        window.blit(self.main_fraim, (self.rect.x, self.rect.y))
        window.blit(pygame.transform.scale2x(player.sprite), (75, 25), (0 , 0, 128, 95))
        window.blit(self.name_fraim, self.name_fraim_position)
        window.blit(self.char_name, self.char_name_position)

        self.heart.updateImage()
        self.heart.draw(window, self.heart.rect.x, self.heart.rect.y)

        for key in player.keys:
            key.updateImage()
            for i in range(len(player.keys)):
                key.draw(window, 75 + i * key.image.get_width(), 125)
        for gear in player.gears:
            gear.updateImage()
            for i in range(len(player.gears)):
                gear.draw(window, 75 + i * gear.image.get_width(), 175)

        window.blit(self.main_object.sprites[3 - len(player.notices)], (450, 0))

        if player.have_screwdriver == True:
            window.blit(player.screwdriver.image, (400, 150))
            player.screwdriver.updateImage()
