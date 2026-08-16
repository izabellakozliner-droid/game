import pygame
import random
import consts
import numpy as np

# def CreateGameField(row, calumn):
#     GameField = []
#     for i in range(calumn):
#         GameField.append([])
#         for j in range(calumn):
#             GameField.append([])
#     return GameField

def CreateGameField(row, calumn):
    GameField = [[0 for _ in range(calumn)] for _ in range(row)]
    return GameField

# def FlagSpawn(GameField):
#     height = 4
#     for i in range (len(GameField)):
#         for j in range (len(GameField[i])):
#             if height> 0:
#                 for k in range(3):
#                     GameField[i + 17][k-1] = 4
#         height = height - 1


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



print(CreateGameField(consts.RowAmount, consts.CallumnAmount))