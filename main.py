import pygame
import sys
sys.path += ["Classes", "Controllers"]

from Classes.MapClass import TileMap
from Classes.PlayerClass import Player
import Controllers.SpriteController as Sprite
import Classes.CameraClass as Camera

pygame.init()
pygame.display.set_caption("Andrei's Crusade")

WIDTH, HEIGHT = 1800, 1000
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface((WIDTH, HEIGHT))

def draw(window, player, offset_x, map, camera):
    Sprite.parallax_background(window, WIDTH, HEIGHT, offset_x)
    map.draw_map(window, camera)
    player.draw(window, camera)
    # window.blit(player.sprite, (player.rect.x - camera.offset.x, player.rect.y - camera.offset.y))
    # window.blit(canvas, (0, 0))

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    player = Player()
    map = TileMap('level_1_mainMap.csv')
    camera = Camera.Camera(player, WIDTH, HEIGHT)
    follow = Camera.Follow(camera, player)
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


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right = False
                elif event.key == pygame.K_SPACE:
                    if player.is_jumping:
                        player.velocity.y *= .25
                        player.is_jumping = False

        player.loop(delta_time, map.tiles)
        camera.scroll()
        
        draw(window, player, offset_x, map, camera)


        # if player.rect.x > PLAYER_START_POSITION + scroll_area_width:
        # if ((player.rect.right - offset_x >= WIDTH - 200) and player.velocity.x > 0) or (
        #     (player.rect.left - offset_x <= 200) and player.velocity.x < 0):
        #         offset_x += player.velocity.x
        # elif ((player.rect.top - offset_y >= HEIGHT - scroll_area_height)) or ((player.rect.bottom - offset_y <= scroll_area_height )):
        #         offset_y += 10

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
