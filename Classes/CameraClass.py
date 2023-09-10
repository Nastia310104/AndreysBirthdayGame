import pygame
from abc import abstractmethod, ABC

vector = pygame.math.Vector2

class Camera:
    def __init__(self, player, width, height):
        self.player = player
        self.offset = vector(0, 0)
        self.offset_float = vector(0, 0)
        self.display_width, self.display_height = width, height
        self.CONST = vector(-self.player.START_POSITION_X + player.rect.w / 2, -self.player.START_POSITION_Y + 20)

    def setmethod(self, method):
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

# class Border(CamScroll):
#     def __init__(self, camera, player):
#         CamScroll.__init__(self, camera, player)

#     def scroll(self):
#         self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
#         self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
#         self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
#         self.camera.offset.x = max(self.player.left_border, self.camera.offset.x)
#         self.camera.offset.x = min(self.camera.offset.x, self.player.right_border - self.camera.DISPLAY_W)

class Auto(CamScroll):
    def __init__(self,camera,player):
        CamScroll.__init__(self,camera,player)

    def scroll(self):
        self.camera.offset.x += 1









