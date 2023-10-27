import pygame
import tkinter

pygame.init()
pygame.font.init()
pygame.mixer.init()

import Controllers.MenuController as Menu, Controllers.SoundsController as Sound
from Classes.EnemyClass import ENEMY_GROUP
from Classes.LevelObjects.BulletClass import BULLET_GROUP
from Classes.LevelClass import Level
import Classes.CameraClass as Camera

screen_info = tkinter.Tk()
 
ICON_PATH = 'Assets/MainObjects/dino.png'
WIDTH, HEIGHT = screen_info.winfo_screenwidth(), screen_info.winfo_screenheight()
FPS = 30

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Andrei's Crusade")
pygame.display.set_icon(pygame.image.load(ICON_PATH))

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
    level = Level(WIDTH, HEIGHT)
    Sound.playBackgroungMusic()
    run = Menu.setMenu(window, level, "start")

    while run:
        pygame.mouse.set_visible(False)
        delta_time = level.clock.tick(FPS) * .001 * 60
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if level.player.is_dead: 
                Menu.setMenu(window, level, "death")

            if event.type == pygame.KEYDOWN and not level.player.is_dieing:
                if event.key == pygame.K_e and level.player.level_complete:
                    Menu.setMenu(window, level, "level_complete")

                if event.key == pygame.K_ESCAPE:
                    Menu.setMenu(window, level)
                    level.player.go_left = False
                    level.player.go_right = False

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    level.player.go_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    level.player.go_right = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if level.player.jump_count < 2:
                        level.player.jump()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    downscroll = Camera.Auto(level.camera)
                    level.camera.setMethod(downscroll)
                elif event.key == pygame.K_SPACE and level.player.is_attack == False:
                    level.player.attack()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    level.player.go_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    level.player.go_right = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if level.player.is_jumping:
                        level.player.velocity.y *= .25
                        level.player.is_jumping = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    level.camera.setMethod(level.follow)

        level.player.loop(delta_time, level.objects)
        level.camera.scroll()

        for enemy in ENEMY_GROUP.sprites():
            enemy.loop(level.map.tiles, level.player)
        for bullet in BULLET_GROUP.sprites():
            bullet.loop(level.map.tiles)

        draw(window, level.player, level.map, level.camera, level.portrait, level.background)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
