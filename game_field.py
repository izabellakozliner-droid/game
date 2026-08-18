import pygame
import random
import consts
import numpy as np

GameField = []
def create_matrix():
    global GameField
    GameField = [50*[i for i in "_"]for j in range(25)]

    return GameField
create_matrix()

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

FlagSpawn(GameField)

Player_matrix = []
def player_matrix():
    global Player_matrix
    Player_matrix = [50*[i for i in "_"]for j in range(25)]
    # Player_matrix = np.zeros((3, 4), dtype=int)

    return Player_matrix
player_matrix()

bomb_matrix = []
def Bomb_matrix():
    global bomb_matrix
    bomb_matrix = [50*[i for i in "_"]for j in range(25)]


    return bomb_matrix
Bomb_matrix()


def MinesGenerator(GameField, Player_matrix, bomb_matrix):
    minesLeft = consts.MinesAmmount
    while minesLeft > 0:
        mineStartRow = random.randint(0, consts.RowAmount - 1)
        mineStartCol = random.randint(0, 47)
        ClearSpace = True
        for i in range(3):
            if GameField[mineStartRow][mineStartCol + i] != "_" or Player_matrix[mineStartRow][mineStartCol + i] != "_" or bomb_matrix[mineStartRow][mineStartCol + i] == -2:
                ClearSpace = False
                break
        #Tryint to prevent mines from blocking the only passage to the flag
        try:
            for i in range(5):
                if bomb_matrix[mineStartRow + i][mineStartCol] == -2 or bomb_matrix[mineStartRow - i][mineStartCol]== -2 or bomb_matrix[mineStartRow + i][mineStartCol + 2] == -2 or bomb_matrix[mineStartRow - i][mineStartCol + 2]== -2:
                    ClearSpace = False
                    break
            for i in range(4):
                if bomb_matrix[mineStartRow][mineStartCol + i] == -2 or bomb_matrix[mineStartRow][mineStartCol - i] == -2:
                    ClearSpace = False
                    break
        except IndexError:
            pass
        if ClearSpace == True:
            for j in range (3):
                bomb_matrix[mineStartRow][mineStartCol + j] = -2
            minesLeft -= 1
    return bomb_matrix
MinesGenerator(GameField,Player_matrix,bomb_matrix)
print(bomb_matrix)
for col in zip(bomb_matrix):
    print(list(col))


def random_grass(random_bomb):
    for item in range(consts.TOTAL_NUM_GRASS):
       col  = random.randint(-1,len(GameField))
       row = random.randint(-1, len(GameField[1]))
       try:
           if GameField[col][row] == "_":
               GameField[col][row] = "GRASS"
           # for col in zip(GameField):
           #     print(list(col))
       except IndexError: #Without it we face a mistake because col max is 50 while it's max index is 49
           pass
    for col in zip(GameField):
        print(list(col)) #moved out of the cycle so it won't print matrix until it is done
    return GameField # moved it out of for loop so it won't end the function when the first grass appears
random_grass(GameField)




