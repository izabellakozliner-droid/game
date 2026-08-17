import consts
import random
import pygame
import game_field

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
    for j in range(len(GameField[0])):#בודק שורה ראשונה במטריצה
        if GameField[0][j] == (1, -1, 5):
            #1 בודק אם החייל במקום ריק
            #-1 בודק אם החייל על פצצה
            #5 בודק אם החייל הגיע לדגל
            return

    for i in range(len(GameField)):#בודק כל שורה בלוח (אינדקס)
        for j in range(len(GameField[i])):#בודק כל עמודה בשורה(אינדקס)
            if GameField[i][j] == 1:#בודק אם המקום בלוח שווה 1 כלומר החייל
                GameField[i-1][j] += 1#זז שורה למעלה ונשאר באותה עמודה
                GameField[i][j] -= 1#המקום שהחייל היה הופך לריק


def MoovementDown(GameField):

    for j in range(len(GameField[24])):#בודק שורה אררונה במטריצה
        if GameField[0][j] == (1, -1, 5):
            # 1 בודק אם החייל במקום ריק
            # -1 בודק אם החייל על פצצה
            # 5 בודק אם החייל הגיע לדגל
            return

    for i in range(len(GameField)):#בודק כל שורה בלוח (אינדקס)
        for j in range(len(GameField[i])):#בודק כל עמודה בשורה(אינדקס)
            if GameField[i][j] == 1:#בודק אם המקום בלוח שווה 1 כלומר החייל
                GameField[i+1][j] += 1#זז שורה למטה ונשאר באותה עמודה
                GameField[i][j] -= 1#המקום שהחייל היה הופך לריק

def MoovementRight(GameField):

    for i in range(len(GameField)):
        if GameField[i][24] == (1, -1, 5):
            return

    for i in range(len(GameField)):
        for j in range(len(GameField[i]) - 1, -1, -1):
            if GameField[i][j] == 1:
                GameField[i][j+1] += 1
                GameField[i][j] -= 1

def MoovementLeft(GameField):

    for i in range(len(GameField)):
        if GameField[i][0] == (1, -1, 5):
            return

    for i in range(len(GameField)):
        for j in range(len(GameField[i])):
            if GameField[i][j] == 1:
                GameField[i][j-1] += 1
                GameField[i][j] -= 1

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







