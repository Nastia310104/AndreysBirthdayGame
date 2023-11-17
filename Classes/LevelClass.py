import pygame
from Classes.MapObjects.MapClass import TileMap
from Classes.PlayerClass import Player
from Classes.WindowObjects.PortraitClass import Portrait
import Classes.CameraClass as Camera
from Classes.WindowObjects.BackgroundClass import Background

LEVEL_1_MAPS = ['Levels/Level_1/level_1_mainMap.csv', 'Levels/Level_1/level_1_mainObjects.csv', 'Levels/Level_1/level_1_enemies.csv']
LEVEL_1_TEST_MAPS = ['Levels/Level_1/test_level_1_mainMap.csv', 'Levels/Level_1/test_level_1_mainObjects.csv', 'Levels/Level_1/level_1_enemies.csv']
LEVEL_1_NEW_MAP = ['Levels/Level_1/level_1_map.csv', 'Levels/Level_1/level_1_Objects.csv', 'Levels/Level_1/level_1_NPS.csv']

class Level():
    def __init__(self, width, height):
        self.level_number = 1
        self.clock = pygame.time.Clock()
# Map
        self.map = TileMap(LEVEL_1_NEW_MAP)
        self.objects = self.map.tiles + self.map.objects + self.map.enemies
# Player
        self.player = Player(self.map.player_position.x, self.map.player_position.y)
# Screen
        self.screen_width, self.screen_height = width, height
        self.portrait = Portrait(75, 0)
        self.background = Background(self.screen_width, self.screen_height)
# Camera
        self.camera = Camera.Camera(self.player, self.screen_width, self.screen_height, self.map)
        self.follow = Camera.Follow(self.camera)
        self.camera.setMethod(self.follow)

    def restartLevel(self):
        self.player.playerReset()
        self.map.redrawLevel()
        self.objects = self.map.tiles + self.map.objects + self.map.enemies
        self.camera.player = self.player
        self.follow.camera = self.camera
