import pygame
import sys
sys.path += ["Classes", "Controllers"]
import tkinter

from Classes.MapClass import TileMap
from Classes.PlayerClass import Player
import Controllers.SpriteController as Sprite
import Classes.CameraClass as Camera
from Classes.EnemyClass import Enemy, ENEMY_GROUP
from Classes.LevelObjects.BulletClass import BULLET_GROUP
 

pygame.init()
pygame.display.set_caption("Andrei's Crusade")
app = tkinter.Tk()

WIDTH, HEIGHT = app.winfo_screenwidth(), app.winfo_screenheight()
FPS = 60

LEVEL_1_MAPS = ['Levels/Level_1/level_1_mainMap.csv', 'Levels/Level_1/level_1_mainObjects.csv', 'Levels/Level_1/level_1_enemies.csv']
LEVEL_1_TEST_MAPS = ['Levels/Level_1/level_1_mainMap.csv', 'Levels/Level_1/test_level_1_mainObjects.csv', 'Levels/Level_1/level_1_enemies.csv']

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window, player, map, camera):
    Sprite.parallax_background(window, WIDTH, HEIGHT, camera.offset.x)
    map.drawMap(window, camera)
    player.draw(window, camera)
    
    for enemy in ENEMY_GROUP.sprites():
        enemy.draw(window, camera)
    for bullet in BULLET_GROUP.sprites():
        bullet.draw(window, camera)


    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    player = Player()
    map = TileMap(LEVEL_1_TEST_MAPS)

    camera = Camera.Camera(player, WIDTH, HEIGHT, map)
    follow = Camera.Follow(camera, player)
    auto = Camera.Auto(camera, player, camera.offset.y)

    camera.setMethod(follow)

    level_objects = map.tiles + map.objects + map.enemies

    run = True
    while run:
        delta_time = clock.tick(FPS) * .001 * FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                player.animation_count = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if player.jump_count < 2:
                        player.jump()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    camera.setMethod(auto)
                elif event.key == pygame.K_SPACE and player.is_attack == False:
                    player.attack()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if player.is_jumping:
                        player.velocity.y *= .25
                        player.is_jumping = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    camera.setMethod(follow)

        player.loop(delta_time, level_objects)
        camera.scroll()

        for enemy in ENEMY_GROUP.sprites():
            enemy.loop(map.tiles, player)

        for bullet in BULLET_GROUP.sprites():
            bullet.loop(map.tiles)

        draw(window, player, map, camera)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
