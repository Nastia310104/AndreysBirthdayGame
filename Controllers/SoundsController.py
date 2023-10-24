import pygame
import random
from os import listdir
from os.path import isfile, join

BACKGROUND_MUSIC_PATH = 'Assets/Sounds/Music/Level1'

# Enemy sounds
ENEMY_ATTACK = pygame.mixer.Sound('Assets/Sounds/SFX/enemy_attack_fun.wav')
ENEMY_HURT = pygame.mixer.Sound('Assets/Sounds/SFX/enemy_hurt.wav')
ENEMY_DIE = pygame.mixer.Sound('Assets/Sounds/SFX/enemy_death.wav')
# Collected sounds
TOOLS_COLLECTED = pygame.mixer.Sound('Assets/Sounds/SFX/tools_collected.wav')
NOTICE_COLLECTED = pygame.mixer.Sound('Assets/Sounds/SFX/collect_notice.wav')
GEAR_OR_KEY_COLLECTED = pygame.mixer.Sound('Assets/Sounds/SFX/gear_collected.wav')
GEAR_OR_KEY_COLLECTED.set_volume(0.8)
HEART_COLLECTED = pygame.mixer.Sound('Assets/Sounds/SFX/collect_heart.wav')
GUN_CHARGED = pygame.mixer.Sound('Assets/Sounds/SFX/battery_collected.wav')
CHEST_OPENED = pygame.mixer.Sound('Assets/Sounds/SFX/chest_opened.wav')
DOOR_OPENS = pygame.mixer.Sound('Assets/Sounds/SFX/door_open_2.wav')
TRAP_APPEARS = pygame.mixer.Sound('Assets/Sounds/SFX/trap_sound.wav')
PLATFORMS_APPER = pygame.mixer.Sound('Assets/Sounds/SFX/platforms_moving.wav')
# PLayer_sounds
PLAYER_DEAD = pygame.mixer.Sound('Assets/Sounds/SFX/gameover.wav')
HIT_WALL = pygame.mixer.Sound('Assets/Sounds/SFX/hitwall.wav')
JUMP = pygame.mixer.Sound('Assets/Sounds/SFX/player_jump.wav')
SHOOT = pygame.mixer.Sound('Assets/Sounds/SFX/shoot.wav')
PLAYER_HURT = pygame.mixer.Sound('Assets/Sounds/SFX/player_hurt.wav')
# Other sounds
BUTTON_HOVER = pygame.mixer.Sound('Assets/Sounds/SFX/button_hover.wav')
BUTTON_HOVER.set_volume(0.6)
BUTTON_PRESSED = pygame.mixer.Sound('Assets/Sounds/SFX/button_pressed.wav')
LEVEL_COMPLETE = pygame.mixer.Sound('Assets/Sounds/SFX/level_finished.wav')
PAZZLE_STARTS = pygame.mixer.Sound('Assets/Sounds/SFX/pazzle_start_tune.wav')

def playBackgroungMusic():
    tracks = [f for f in listdir(BACKGROUND_MUSIC_PATH) if isfile(join(BACKGROUND_MUSIC_PATH, f))]
    playMusic = True

    if playMusic:
        pygame.mixer.music.load(BACKGROUND_MUSIC_PATH + '/' +random.choice(tracks))
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)