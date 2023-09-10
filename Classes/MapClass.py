import pygame, csv, os, array
from Classes.BlockClass import Block, BLOCK_GROUP
from Classes.LevelObjects.ChestClass import Chest, CHEST_GROUP
from Classes.LevelObjects.GearClass import Gear, GEAR_GROUP
from Classes.LevelObjects.NoticeClass import Notice, NOTICE_GROUP

GAP = 64
TILESET_PATH = "Assets/Tiles/"
TILE_NAME = "Tile_"
OBJECTS_PATH = "Assets/LevelObjects/"
OBJECT_NAME = "Object_"

class TileMap():
    def __init__(self, filename, objects_filename):
        self.tile_size = 64
        self.start_x = 0
        self.start_y = 0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_width, self.map_height))
        self.map_surface.set_colorkey((0, 0, 0))
        self.objects = self.load_objects(objects_filename)
        self.load_map()

    def draw_map(self, window, camera):
        window.blit(self.map_surface, (0 - camera.offset.x, 0 - camera.offset.y))
        for object in (GEAR_GROUP.sprites() + NOTICE_GROUP.sprites()):
            object.update_image()
            window.blit(object.image, (object.rect.x - camera.offset.x, object.rect.y - camera.offset.y))

    def load_map(self):
        BLOCK_GROUP.draw(self.map_surface)
        CHEST_GROUP.draw(self.map_surface)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))

        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
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
    
    def load_objects(self, object_filename):
        objects = []
        object_map = self.read_csv(object_filename)
        y = 0
        for row in object_map:
            x = 0
            for object in row:
                if int(object) == 0:
                    objects.append(Notice(x * 64, y * 64))
                elif int(object) == 1:
                    objects.append(Chest(x * 64, y * 64, self.map_surface))
                elif int(object) == 2:
                    objects.append(Gear(x * 64, y * 64))
                elif int(object) > 2:
                    objects.append(Block((OBJECTS_PATH + OBJECT_NAME + str(object) + '.png'), x * 64, y * 64))
                x += 1
            y += 1
        return objects
