import pygame
import consts
import game_field
import solider

matrix = game_field.CreateGameField(25, 50)
for col in zip(matrix):
    print(list(col))

print(matrix)

def HandleInput(events):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    solider.MoovementUP(matrix)
                elif event.key == pygame.K_DOWN:
                    solider.MoovementDown(matrix)
                elif event.key == pygame.K_LEFT:
                    solider.MoovementLeft(matrix)
                elif event.key == pygame.K_RIGHT:
                    solider.MoovementRight(matrix)
