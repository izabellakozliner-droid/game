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
        for col in zip(Player_matrix):
            print(list(col))



def MoovementDown(Player_matrix):
    if soldier_pos["row"] + consts.PLAYER_HEIGHT < 25:
        ClearSoldier(Player_matrix)
        soldier_pos["row"] += 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.y += 25
        for col in zip(Player_matrix):
            print(list(col))


def MoovementRight(Player_matrix):
    if soldier_pos["col"] + consts.PLAYER_WIDTH < 49:
        ClearSoldier(Player_matrix)
        soldier_pos["col"] += 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.x += 25
        for col in zip(Player_matrix):
            print(list(col))

def MoovementLeft(Player_matrix):
    if soldier_pos["col"] > 0:
        ClearSoldier(Player_matrix)
        soldier_pos["col"] -= 1
        DrawSoldier(Player_matrix)
        main.PlayerPos.x -= 25
        for col in zip(Player_matrix):
            print(list(col))


def StopOnTheMine(bomb_matrix, Player_matrix):
    for i in range (len(Player_matrix)):
        for j in range (len(Player_matrix[i])):
            if Player_matrix[i][j] == 1:
                if bomb_matrix[i][j] == -2:
                    # print("You Lost!")
                    return True



def StopOnFlag(GameField, Player_matrix):
    for i in range(len(Player_matrix)):
        for j in range(len(Player_matrix[i])):
            try:
                if Player_matrix[i][j] == 1:
                    if GameField[i][j] == 4:
                        # print("You Win!")
                        return True
            except IndexError:
                pass







