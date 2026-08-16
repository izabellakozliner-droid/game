import pygame
import random
import consts
import numpy as np

import solider

# def CreateGameField(row, calumn):
#     GameField = []
#     for i in range(calumn):
#         GameField.append([])
#         for j in range(calumn):
#             GameField.append([])
#     return GameField

# def CreateGameField(row, calumn):
#     GameField = [[0 for _ in range(calumn)] for _ in range(row)]
#     return GameField
#
# print(CreateGameField(consts.RowAmount, consts.CallumnAmount))

# def random_grass():
#     grass_image = pygame.image.load("grass.png")
#
#     grass_display = grass_image[random.randint(0,20)]

GameField = []
def create_matrix():
    global GameField
    GameField = [50*[i for i in " "] for j in range(25)]
    return GameField
print(create_matrix())


solider.StartSoldierPos(GameField)
solider.


for col in zip(GameField):
    print(list(col))
