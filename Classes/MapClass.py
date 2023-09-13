import pygame, csv, os, array
from Classes.BlockClass import Block, BLOCK_GROUP
from Classes.LevelObjects.ChestClass import Chest, CHEST_GROUP
from Classes.LevelObjects.GearClass import Gear, GEAR_GROUP
from Classes.LevelObjects.NoticeClass import Notice, NOTICE_GROUP
from Classes.EnemyClass import Enemy
from Classes.LevelObjects.BatteryClass import Battery, BATTERY_GROUP
from Classes.LevelObjects.KeyClass import Key, KEY_GROUP
from Classes.LevelObjects.GunClass import GUN_GROUP
from Classes.LevelObjects.ScrewdriverClass import SCREWDRIVER_GROUP

GAP = 64
TILESET_PATH = "Assets/Tiles/"
TILE_NAME = "Tile_"
OBJECTS_PATH = "Assets/LevelObjects/"
OBJECT_NAME = "Object_"
FIRST_LEVEL_CHEST_CONTENT = ['gun', 'screwdriver']

class TileMap():
    def __init__(self, filenames):
        self.tile_size = 64
        self.start_x = 0
        self.start_y = 0
        self.tiles = self.loadTiles(filenames[0])
        self.objects = self.loadObjects(filenames[1])
        self.enemies = self.loadNps(filenames[2])
        self.map_surface = pygame.Surface((self.map_width, self.map_height))
        self.map_surface.set_colorkey((0, 0, 0))
        self.fillMap()

    def drawMap(self, window, camera):
        window.blit(self.map_surface, (0 - camera.offset.x, 0 - camera.offset.y))
        for object in (GEAR_GROUP.sprites() + NOTICE_GROUP.sprites() + BATTERY_GROUP.sprites() + KEY_GROUP.sprites() + CHEST_GROUP.sprites() + GUN_GROUP.sprites() + SCREWDRIVER_GROUP.sprites()):
            object.updateImage()
            window.blit(object.image, (object.rect.x - camera.offset.x, object.rect.y - camera.offset.y))

    def fillMap(self):
        BLOCK_GROUP.draw(self.map_surface)

    def readCsv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))

        return map
    
    def loadMap(self, filenames):
        return self.loadTiles(filenames[0]) + self.loadObjects(filenames[1]) + self.loadNps(filenames[2])
    
    def loadTiles(self, filename):
        tiles = []
        map = self.readCsv(filename)
        y = 0
        for row in map:
            x = 0
            for tile in row:
                if int(tile) > GAP and int(tile) <= GAP+9:
                    block =Block((TILESET_PATH + TILE_NAME + '0' + str(int(tile) - GAP) + '.png'), x * self.tile_size, y * self.tile_size)
                elif int(tile) > GAP + 9:
                    block = Block((TILESET_PATH + TILE_NAME + str(int(tile) - GAP) + '.png'), x * self.tile_size, y * self.tile_size)
                tiles.append(block)
                x += 1
            y += 1

        self.map_width, self.map_height = x * self.tile_size, y * self.tile_size

        return tiles
    
    def loadObjects(self, object_filename):
        objects = []
        object_map = self.readCsv(object_filename)
        y = 0
        i = 0
        for row in object_map:
            x = 0
            for object in row:
                match int(object):
                    case 0: objects.append(Notice(x * 64, y * 64))
                    case 1: 
                        objects.append(Chest(x * 64, y * 64, FIRST_LEVEL_CHEST_CONTENT[i]))
                        i += 1
                    case 2: objects.append(Gear(x * 64, y * 64))
                    case 3: objects.append(Key(x * 64, y * 64))
                    case 5: objects.append(Battery(x * 64, y * 64))
                x += 1
            y += 1

        return objects
    
    def loadNps(self, nps_map_filename):
        NPSs = []
        nps_map = self.readCsv(nps_map_filename)
        y = 0
        for row in nps_map:
            x = 0
            for nps in row:
                if int(nps) == 6:
                    NPSs.append(Enemy(x * 64, y * 64))
                x += 1
            y += 1

        return NPSs
