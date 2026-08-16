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

def random_grass():
    for item in range(consts.TOTAL_NUM_BOMB):


