import consts
import random
import pygame
import game_field

def StartSoldierPos(Player_matrix):
    Player_matrix[0][0] = 1
    Player_matrix[0][1] = 1
    Player_matrix[1][0] = 1
    Player_matrix[1][1] = 1
    Player_matrix[2][0] = 1
    Player_matrix[2][1] = 1
    Player_matrix[3][0] = 1
    Player_matrix[3][1] = 1
    return Player_matrix

def MoovementUP(Player_matrix):
    for j in range(len(Player_matrix[0])):#בודק שורה ראשונה במטריצה
        if Player_matrix[0][j] == (1):
            #1 בודק אם החייל במקום ריק
            #-1 בודק אם החייל על פצצה
            #5 בודק אם החייל הגיע לדגל
            return

    for i in range(len(Player_matrix)):#בודק כל שורה בלוח (אינדקס)
        for j in range(len(Player_matrix[i])):#בודק כל עמודה בשורה(אינדקס)
            if Player_matrix[i][j] == 1:#בודק אם המקום בלוח שווה 1 כלומר החייל
                Player_matrix[i-1][j] += 1#זז שורה למעלה ונשאר באותה עמודה
                Player_matrix[i][j] -= 1#המקום שהחייל היה הופך לריק


def MoovementDown(Player_matrix):

    for j in range(len(Player_matrix[24])):#בודק שורה אררונה במטריצה
        if Player_matrix[0][j] == (1):
            # 1 בודק אם החייל במקום ריק
            # -1 בודק אם החייל על פצצה
            # 5 בודק אם החייל הגיע לדגל
            return

    for i in range(len(Player_matrix)):#בודק כל שורה בלוח (אינדקס)
        for j in range(len(Player_matrix[i])):#בודק כל עמודה בשורה(אינדקס)
            if Player_matrix[i][j] == 1:#בודק אם המקום בלוח שווה 1 כלומר החייל
                Player_matrix[i+1][j] += 1#זז שורה למטה ונשאר באותה עמודה
                Player_matrix[i][j] -= 1#המקום שהחייל היה הופך לריק

def MoovementRight(Player_matrix):

    for i in range(len(Player_matrix)):
        if Player_matrix[i][24] == (1):
            return

    for i in range(len(Player_matrix)):
        for j in range(len(Player_matrix[i]) - 1, -1, -1):
            if Player_matrix[i][j] == 1:
                Player_matrix[i][j+1] += 1
                Player_matrix[i][j] -= 1

def MoovementLeft(Player_matrix):

    for i in range(len(Player_matrix)):
        if Player_matrix[i][0] == (1):
            return

    for i in range(len(Player_matrix)):
        for j in range(len(Player_matrix[i])):
            if Player_matrix[i][j] == 1:
                Player_matrix[i][j-1] += 1
                Player_matrix[i][j] -= 1

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







