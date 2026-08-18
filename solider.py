import consts
import random
import pygame
import game_field
import main

soldier_pos = {"row": 0, "col": 0}

def ClearSoldier(Player_matrix):
    for r in range(consts.SOLDIER_ROW, consts.SOLDIER_ROW + consts.PlayerMatrixHigh):
        for c in range(consts.SOLDIER_COL, consts.SOLDIER_COL + consts.PlayerMatrixWidth):
            if (0 <= r < len(Player_matrix) and 0 <= c < len(Player_matrix[0]) and Player_matrix[r][c] == 1):
                Player_matrix[r][c] = "_"


def DrawSoldier(Player_matrix):
    for r in range(consts.SOLDIER_ROW, consts.SOLDIER_ROW + consts.PlayerMatrixHigh):
        for c in range(consts.SOLDIER_COL, consts.SOLDIER_COL + consts.PlayerMatrixWidth):
            if 0 <= r < len(Player_matrix) and 0 <= c < len(Player_matrix[0]):
                Player_matrix[r][c] = 1
    for col in zip(Player_matrix):
        print(list(col))

# if soldier_pos["row"] > 0:
#         ClearSoldier(Player_matrix)
#         soldier_pos["row"] -= 1
#         DrawSoldier(Player_matrix)
#         main.PlayerPos.y -= 25




def UP():
    if consts.SOLDIER_ROW > 0:
        consts.SOLDIER_ROW -= 1
        print("SOLDIER_ROW: ", consts.SOLDIER_ROW)


def Down():
    if consts.SOLDIER_ROW< 25:
        consts.SOLDIER_ROW += 1
        print("SOLDIER_ROW: ", consts.SOLDIER_ROW)


def Right():
    if consts.SOLDIER_COL < 49:
        consts.SOLDIER_COL += 1
        print("SOLDIER_col: ", consts.SOLDIER_COL)


def Left():
    if consts.SOLDIER_COL > 0:
        consts.SOLDIER_COL -= 1
        print("SOLDIER_col: ", consts.SOLDIER_COL)


def StopOnTheMine(bomb_matrix, Player_matrix):
    for i in range(len(bomb_matrix)):
        for j in range(len(bomb_matrix[i])):
            if bomb_matrix[i][j] == -2:
                if i == consts.SOLDIER_ROW and j == consts.SOLDIER_COL:
                    print("You Lost!")
                    return True


def StopOnFlag(GameField, Player_matrix):
    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == 4:
                if i == consts.SOLDIER_ROW and j == consts.SOLDIER_COL:
                    print("You Win!")
                    return True
