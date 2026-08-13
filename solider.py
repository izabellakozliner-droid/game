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

def MoovementUP(GameField):
    for i in range(GameField):
        for j in range(GameField):
            if GameField[i][j] == 1:
                try:
                    GameField[i+1][j] = 1
                    game_field[i][j] = 0
                except IndexError:
                    pass

def MoovementDown(GameField):
    for i in range(GameField):
        for j in range(GameField):
            if GameField[i][j] == 1:
                try:
                    GameField[i-1][j] += 1
                    game_field[i][j] -= 0
                except IndexError:
                    pass

def MoovementRight(GameField):
    for i in range(GameField):
        for j in range(GameField):
            if GameField[i][j] == 1:
                try:
                    GameField[i][j+1] = 1
                    game_field[i][j] = 0
                except IndexError:
                    pass

def MoovementLeft(GameField):
    for i in range(GameField):
        for j in range(GameField):
            if GameField[i][j] == 1:
                try:
                    GameField[i][j-1] = 1
                    game_field[i][j] = 0
                except IndexError:
                    pass

def StopOnTheMine(GameField):
    for i in range(GameField):
        for j in range(GameField):
            if GameField[i][j] == 3:
                return True

def StopOnFlag(GameField):
    for i in range(GameField):
        for j in range(GameField):
            if GameField[i][j] == 4:
                return True






