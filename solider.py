import consts
import random
import pygame
import game_field
import main


def ClearSoldier(Player_matrix):
    for r in range(consts.SOLDIER_ROW, consts.SOLDIER_ROW + consts.PLAYER_HEIGHT):
        for c in range(consts.SOLDIER_COL, consts.SOLDIER_COL + consts.PLAYER_WIDTH):
            if (0 <= r < len(Player_matrix) and 0 <= c < len(Player_matrix[0]) and Player_matrix[r][c] == 1):
                Player_matrix[r][c] = "_"


def DrawSoldier(Player_matrix):
    for r in range(consts.SOLDIER_ROW, consts.SOLDIER_ROW + consts.PLAYER_HEIGHT):
        for c in range(consts.SOLDIER_COL, consts.SOLDIER_COL + consts.PLAYER_WIDTH):
            if 0 <= r < len(Player_matrix) and 0 <= c < len(Player_matrix[0]):
                Player_matrix[r][c] = 1
    for col in zip(Player_matrix):
        print(list(col))


def UP():
    consts.SOLDIER_ROW -= 1
    print("SOLDIER_ROW: ", consts.SOLDIER_ROW)


def Down():
    consts.SOLDIER_ROW += 1
    print("SOLDIER_ROW: ", consts.SOLDIER_ROW)


def Right():
    consts.SOLDIER_COL += 1
    print("SOLDIER_col: ", consts.SOLDIER_COL)


def Left():
    consts.SOLDIER_COL -= 1
    print("SOLDIER_col: ", consts.SOLDIER_COL)


def StopOnTheMine(bomb_matrix, Player_matrix):
    for i in range(len(Player_matrix)):
        for j in range(len(Player_matrix[i])):
            if Player_matrix[i][j] == 1:
                if bomb_matrix[i][j] == -2:
                    print("You Lost!")
                    return True


def StopOnFlag(GameField, Player_matrix):
    for i in range(len(Player_matrix)):
        for j in range(len(Player_matrix[i])):
            if Player_matrix[i][j] == 1:
                if GameField[i][j] == 4:
                    print("You Win!")
                    return True
