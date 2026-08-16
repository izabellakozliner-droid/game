import pygame
import random
import consts
import numpy as np

import solider


# from main import GameField

def CreateGameField(row, calumn):
    GameField = [[0 for _ in range(calumn)] for _ in range(row)]
    return GameField


# def random_grass():
#     grass_image = pygame.image.load("grass.png")
#
#     grass_display = grass_image[random.randint(0,20)]



def FlagSpawn(GameField):
    GameField[24][49] = 4
    GameField[24][48] = 4
    GameField[24][47] = 4
    GameField[23][49] = 4
    GameField[23][48] = 4
    GameField[23][47] = 4
    GameField[22][49] = 4
    GameField[22][48] = 4
    GameField[22][47] = 4
    GameField[21][49] = 4
    GameField[21][48] = 4
    GameField[21][47] = 4

def MinesGenerator(GameField):
    minesLeft = consts.MinesAmmount
    while minesLeft > 0:
        mineStartRow = random.randint(0, consts.RowAmount - 1)
        mineStartCol = random.randint(0, consts.CallumnAmount - 1)
        try:
            if GameField[mineStartRow][mineStartCol] == 0 and GameField[mineStartRow][mineStartCol + 3] == 0 and mineStartCol < 48:
                for i in range (3):
                    GameField[mineStartRow][mineStartCol + i - 1] = -2
                minesLeft -= 1
        except IndexError:
            pass
    return GameField
