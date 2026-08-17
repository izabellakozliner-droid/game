import consts
import random
import pygame
import game_field
import main
soldier_pos = {"row": 0, "col": 0}



def ClearSoldier(Player_matrix):
    for r in range(soldier_pos["row"], soldier_pos["row"] + consts.PLAYER_HEIGHT):
        for c in range(soldier_pos["col"], soldier_pos["col"] + consts.PLAYER_WIDTH):
            if (0 <= r < len(Player_matrix) and 0 <= c < len(Player_matrix[0]) and Player_matrix[r][c] == 1):
                Player_matrix[r][c] = "_"

def DrawSoldier(Player_matrix):
    for r in range(soldier_pos["row"], soldier_pos["row"] + consts.PLAYER_HEIGHT):
        for c in range(soldier_pos["col"], soldier_pos["col"] + consts.PLAYER_WIDTH):
            if 0 <= r < len(Player_matrix) and 0 <= c < len(Player_matrix[0]):
                Player_matrix[r][c] = 1
    for col in zip(Player_matrix):
        print(list(col))



def MoovementUP(Player_matrix):
    if soldier_pos["row"] > 0:
        ClearSoldier(Player_matrix)
        soldier_pos["row"] -= 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.y -= 25



def MoovementDown(Player_matrix):
    if soldier_pos["row"] + consts.PLAYER_HEIGHT < 24:
        ClearSoldier(Player_matrix)
        soldier_pos["row"] += 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.y += 25


def MoovementRight(Player_matrix):
    if soldier_pos["col"] + consts.PLAYER_WIDTH < 49:
        ClearSoldier(Player_matrix)
        soldier_pos["col"] += 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.x += 25

def MoovementLeft(Player_matrix):
    if soldier_pos["col"] > 0:
        ClearSoldier(Player_matrix)
        soldier_pos["col"] -= 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.x -= 25


def StopOnTheMine(GameField):
    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == -1:
                return True

def StopOnFlag(GameField):
    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == 5:
                return True







