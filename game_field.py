import pygame
import random
import consts
import numpy as np


GameField = []
def create_matrix():
    global GameField
    GameField = [50*[i for i in "_"]for j in range(25)]

    for col in zip(GameField):
        print(list(col))
    return GameField
create_matrix()

def FlagSpawn(GameField):
    for i in range(21, 25):
        for j in range(47, 50):
            GameField[i][j] = 4

Player_matrix = []
def player_matrix():
    global Player_matrix
    Player_matrix = [50*[i for i in "_"]for j in range(25)]

    for col in zip(Player_matrix):
        print(list(col))
    return Player_matrix
player_matrix()

bomb_matrix = []
def Bomb_matrix():
    global bomb_matrix
    bomb_matrix = [50*[i for i in "_"]for j in range(25)]

    for col in zip(bomb_matrix):
        print(list(col))
    return bomb_matrix
Bomb_matrix()


def MinesGenerator(GameField, Player_matrix, bomb_matrix):
    minesLeft = consts.MinesAmmount * 10
    while minesLeft > 0:
        mineStartRow = random.randint(0, consts.RowAmount - 1)
        mineStartCol = random.randint(0, 47)
        ClearSpace = True
        for i in range(3):
            if GameField[mineStartRow][mineStartCol + i] != "_" or Player_matrix[mineStartRow][mineStartCol + i] != "_" or bomb_matrix[mineStartRow][mineStartCol + i] == -2:
                ClearSpace = False
                break
        if ClearSpace == True:
            for j in range (3):
                bomb_matrix[mineStartRow][mineStartCol + j] = -2
            minesLeft -= 1
    return bomb_matrix



FlagSpawn(GameField)
MinesGenerator(GameField, Player_matrix, bomb_matrix)
print(bomb_matrix)
for col in zip(bomb_matrix):
    print(list(col))

def random_grass():
    for item in range(consts.TOTAL_NUM_BOMB):
        pass


