import pygame, csv, os
from Classes.BlockClass import Block

GAP = 64
TILESET_PATH = "Assets/1 Tiles/"
TILE_NAME = "Tile_"

class TileMap():
    def __init__(self, filename):
        self.tile_size = 64
        self.start_x = 0
        self.start_y = 0
        self.tiles = self.load_tiles(filename)

    def load_map(self, window):
        for tile in self.tiles:
            tile.draw(window)

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
                if int(tile) > 64 and int(tile) <= 64+9:
                    tiles.append(Block((TILESET_PATH + TILE_NAME + '0' + str(int(tile) - GAP) + '.png'), x * self.tile_size, y * self.tile_size))
                elif int(tile) > 64 + 9:
                    tiles.append(Block((TILESET_PATH + TILE_NAME + str(int(tile) - GAP) + '.png'), x * self.tile_size, y * self.tile_size))
                x += 1
            y += 1

        self.map_width, self.map_height = x * self.tile_size, y * self.tile_size

        return tiles