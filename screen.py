import pygame
import random
import sys
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
    print("newScreen")
    screen.fill((155,155,155))
    pygame.display.update()

def print_screen():
    screen.fill((0,0,0))
    flagSpawn()
    solider_image()
    pygame.display.update()



