import pygame
import random
import sys
import consts,time
import game_field

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def grass_image(screen, GameField):
    GRASS_IMG = pygame.image.load("grass.png").convert_alpha()

    grass_scaled = pygame.transform.scale(
        GRASS_IMG,
        (consts.GRASS_WIDTH, consts.GRASS_HEIGHT)
    )

    for row in range(len(GameField)):
        for col in range(len(GameField[row])):
            if GameField[row][col] == "GRASS":
                x = col * consts.GRASS_WIDTH
                y = row * consts.GRASS_HEIGHT
                screen.blit(grass_scaled, (x, y))

def bomb_image(screen, GameField):
    BOMB_IMG = pygame.image.load("mine.png").convert_alpha()

    bomb_scaled = pygame.transform.scale(
        BOMB_IMG,
        (consts.BOMB_WIDTH, consts.BOMB_HEIGHT)
    )

    for row in range(len(GameField)):
        for col in range(len(GameField[row])):
            if GameField[row][col] == "BOMB":
                x = col * consts.GRASS_WIDTH
                y = row * consts.GRASS_HEIGHT
                screen.blit(bomb_scaled, (x, y))

def flagSpawn():
    FLAG = pygame.image.load("flag.png").convert_alpha()
    scaled_flag = pygame.transform.scale(FLAG, (consts.FLAG_HEIGHT,consts.FLAG_WIDTH))
    screen.blit(scaled_flag, (60, 80))

def solider_image():
    SOLIDER = pygame.image.load('soldier.png')
    soldier = pygame.transform.scale(SOLIDER, (consts.PLAYER_WIDTH, consts. PLAYER_HEIGHT))
    screen.blit(soldier, (200,100))

def newScreen():
    global SCREEN
    screen_color = (0,0,0)
    pygame.display.update()
    screen.fill(screen_color)
    SCREEN = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    drawGrid()
    pygame.display.flip()

def drawGrid():
    pygame.init()
    for row in range(0, consts.WINDOW_WIDTH,consts.BLOCK_SIZE):
        for col in range(0, consts.WINDOW_HEIGHT, consts.BLOCK_SIZE):
            rect = pygame.Rect(row,col,consts.BLOCK_SIZE,consts.BLOCK_SIZE)
            pygame.draw.rect(screen,consts.LINE_COLOR,rect,1)

def print_screen():
    screen.fill((0, 100, 0))
    flagSpawn()
    solider_image()
    # pygame.display.set_caption("The Flag")
    # soldier_image = pygame.image.load("soldier.png")
    # flag_image = pygame.image.load("flag.png")
    # mine_image = pygame.image.load("mine.png")
    # grass_image = pygame.image.load("grass.png")
    pygame.display.update()
    grass_image(screen,game_field.GameField)

