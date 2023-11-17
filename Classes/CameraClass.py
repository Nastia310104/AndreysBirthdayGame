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
        self.CONST = vector(-self.player.start_position_x + (player.rect.w / 2) - width // 2, -self.player.start_position_y + height // 2)
        self.map = map

    def setMethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()

class CamScroll(ABC):
    def __init__(self, camera):
        self.camera = camera

    @abstractmethod
    def scroll(self):
        pass

class Follow(CamScroll):
    def __init__(self, camera):
        CamScroll.__init__(self, camera)

    def scroll(self):
        self.camera.offset_float.x += (self.camera.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.camera.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        self.camera.offset.x = max(0, self.camera.offset.x)
        self.camera.offset.x = min(self.camera.offset.x, self.camera.map.map_width - self.camera.display_width)
        self.camera.offset.y = max(0, self.camera.offset.y)
        self.camera.offset.y = min(self.camera.offset.y, self.camera.map.map_height - self.camera.display_height)

class Auto(CamScroll):
    def __init__(self, camera):
        CamScroll.__init__(self, camera)
        self.start_position = camera.offset.y

    def scroll(self):
        if (self.camera.offset.y < self.start_position + SCROLL_DOWN_LIMIT):
            self.camera.offset.y += 10

        self.camera.offset.y = min(self.camera.offset.y, self.camera.map.map_height - self.camera.display_height)
