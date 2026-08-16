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

# def CreateGameField(row, calumn):
#     GameField = [[0 for _ in range(calumn)] for _ in range(row)]
#     return GameField
#
# print(CreateGameField(consts.RowAmount, consts.CallumnAmount))

# def random_grass():
#     grass_image = pygame.image.load("grass.png")
#
#     grass_display = grass_image[random.randint(0,20)]

game_field = []
def create_matrix():
    global game_field
    game_field = [50*[i for i in " "] for j in range(25)]
    return game_field