import pygame
import random
import consts,time
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
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
    pygame.display.update()



