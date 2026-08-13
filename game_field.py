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

print(CreateGameField(consts.RowAmount, consts.CallumnAmount))