import consts
import random
import pygame
import game_field

# def StartSoldierPos(GameField, SoldierWidth, SoldierHeight):
#     high = consts.SoldierHeight
#     width = consts.SoldierWidth
#     for i in range(len(GameField)):
#         if high > 0:
#             for j in range(len(GameField[i])):
#                 while width > 0:
#                     GameField[i][j] = 1
#                     width -= 1
#                 high -= 1
#     return(GameField)

def StartSoldierPos(GameField):
    GameField[0][0] = 1
    GameField[0][1] = 1
    GameField[1][0] = 1
    GameField[1][1] = 1
    GameField[2][0] = 1
    GameField[2][1] = 1
    GameField[3][0] = 1
    GameField[3][1] = 1
    return GameField

def MoovementUP(GameField):
    for j in range(len(GameField[0])):
        if GameField[0][j] == (1, -1, 5):
            return

    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == 1:
                GameField[i-1][j] += 1
                game_field[i][j] -= 0


def MoovementDown(GameField):

    for j in range(len(GameField[24])):
        if GameField[0][j] == (1, -1, 5):
            return

    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == 1:
                GameField[i+1][j] += 1
                game_field[i][j] -= 0

def MoovementRight(GameField):

    for i in range(len(GameField)):
        if GameField[i][24] == (1, -1, 5):
            return

    for i in range(len(GameField)):
        for j in range(len(GameField[i]) - 1, -1, -1):
            if GameField[i][j] == 1:
                GameField[i][j+1] += 1
                game_field[i][j] -= 0

def MoovementLeft(GameField):

    for i in range(len(GameField)):
        if GameField[i][0] == (1, -1, 5):
            return

    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == 1:
                GameField[i][j-1] += 1
                game_field[i][j] -= 0

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







