import pygame
import sys
sys.path += ["Classes", "Controllers"]
import tkinter

from Classes.MapClass import TileMap
from Classes.PlayerClass import Player
import Controllers.SpriteController as Sprite
import Classes.CameraClass as Camera

pygame.init()
pygame.display.set_caption("Andrei's Crusade")
app = tkinter.Tk()

WIDTH, HEIGHT = app.winfo_screenwidth(), app.winfo_screenheight()
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window, player, offset_x, map, camera):
    Sprite.parallax_background(window, WIDTH, HEIGHT, camera.offset.x)
    map.draw_map(window, camera)
    player.draw(window, camera)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    player = Player()
    map = TileMap('level_1_mainMap.csv')
    camera = Camera.Camera(player, WIDTH, HEIGHT)
    follow = Camera.Follow(camera, player)
    camera.setmethod(follow)

    camera = Camera.Camera(player, WIDTH, HEIGHT, map)
    follow = Camera.Follow(camera, player)
    auto = Camera.Auto(camera, player, camera.offset.y)

    camera.setmethod(follow)

    offset_x = 0

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
                elif event.key == pygame.K_SPACE:
                    if player.jump_count < 2:
                        player.jump()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    camera.setmethod(auto)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right = False
                elif event.key == pygame.K_SPACE:
                    if player.is_jumping:
                        player.velocity.y *= .25
                        player.is_jumping = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    camera.setmethod(follow)

        player.loop(delta_time, map.tiles)
        camera.scroll()

        draw(window, player, offset_x, map, camera)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
