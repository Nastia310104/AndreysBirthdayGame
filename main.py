import pygame
import tkinter

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Andrei's Crusade")

import Classes.CameraClass as Camera
import Controllers.MenuController as Menu, Controllers.SpriteController as Sprite, Controllers.SoundsController as Sound
from Classes.MapObjects.MapClass import TileMap
from Classes.PlayerClass import Player
from Classes.EnemyClass import ENEMY_GROUP
from Classes.LevelObjects.BulletClass import BULLET_GROUP
from Classes.WindowObjects.PortraitClass import Portrait
from Classes.WindowObjects.BackgroundClass import Background

screen_info = tkinter.Tk()
 
WIDTH, HEIGHT = screen_info.winfo_screenwidth(), screen_info.winfo_screenheight()
FPS = 30

LEVEL_1_MAPS = ['Levels/Level_1/level_1_mainMap.csv', 'Levels/Level_1/level_1_mainObjects.csv', 'Levels/Level_1/level_1_enemies.csv']
LEVEL_1_TEST_MAPS = ['Levels/Level_1/test_level_1_mainMap.csv', 'Levels/Level_1/test_level_1_mainObjects.csv', 'Levels/Level_1/level_1_enemies.csv']

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window, player, map, camera, portrait, background):
    background.parallax_background(window, camera.offset.x)
    map.drawMap(window, camera)
    
    for enemy in ENEMY_GROUP.sprites():
        enemy.draw(window, camera)
    for bullet in BULLET_GROUP.sprites():
        bullet.draw(window, camera)
        
    portrait.draw(window, player)
    player.draw(window, camera)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    player = Player()
    map = TileMap(LEVEL_1_TEST_MAPS)
    portrait = Portrait(75, 0)
    camera = Camera.Camera(player, WIDTH, HEIGHT, map)
    follow = Camera.Follow(camera)
    camera.setMethod(follow)
    background = Background(WIDTH, HEIGHT)
    level_objects = map.tiles + map.objects + map.enemies

    Sound.playBackgroungMusic()

    run = Menu.setMenu(window, clock, "start")

    while run:
        delta_time = clock.tick(FPS) * .001 * 60
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if player.is_dead: 
                Menu.setMenu(window, clock, "death")

            if event.type == pygame.KEYDOWN and not player.is_dieing:
                if event.key == pygame.K_e and player.level_complete:
                    Menu.setMenu(window, clock, "level_complete")

                if event.key == pygame.K_ESCAPE:
                    Menu.setMenu(window, clock)
                    player.go_left = False
                    player.go_right = False

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if player.jump_count < 2:
                        player.jump()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    auto = Camera.Auto(camera)
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

        draw(window, player, map, camera, portrait, background)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
