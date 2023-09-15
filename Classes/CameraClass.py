# TODO: Recount camera's offset
# TODO: Recount camera's down scroll

import pygame
from abc import abstractmethod, ABC

vector = pygame.math.Vector2

SCROLL_DOWN_LIMIT = 300

class Camera():
    def __init__(self, player, width, height, map):
        self.player = player
        self.offset = vector(0, 0)
        self.offset_float = vector(0, 0)
        self.display_width, self.display_height = width, height
        self.CONST = vector(-self.player.START_POSITION_X + (player.rect.w / 2) - 400, -self.player.START_POSITION_Y + 150)
        self.map = map

    def setMethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()

class CamScroll(ABC):
    def __init__(self, camera,player):
        self.camera = camera
        self.player = player

    @abstractmethod
    def scroll(self):
        pass

class Follow(CamScroll):
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)

    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        self.camera.offset.x = max(0, self.camera.offset.x)
        self.camera.offset.x = min(self.camera.offset.x, self.camera.map.map_width - self.camera.display_width)
        self.camera.offset.y = max(0, self.camera.offset.y)
        self.camera.offset.y = min(self.camera.offset.y, self.camera.map.map_height - self.camera.display_height)

class Auto(CamScroll):
    def __init__(self,camera,player, start_position):
        CamScroll.__init__(self,camera,player)
        self.start_position = start_position

    def scroll(self):
        if (self.camera.offset.y < self.start_position + SCROLL_DOWN_LIMIT):
            self.camera.offset.y += 10

        self.camera.offset.y = min(self.camera.offset.y, self.camera.map.map_height - self.camera.display_height)
