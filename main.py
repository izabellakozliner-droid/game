import pygame
import consts
import game_field
import solider


GameField = game_field.CreateGameField(consts.RowAmount, consts.CallumnAmount)
solider.StartSoldierPos(GameField, consts.SoldierWidth, consts.SoldierHeight)

def HandleInput(events):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    solider.MoovementUP(GameField)
                elif event.key == pygame.K_DOWN:
                    solider.MoovementDown(GameField)
                elif event.key == pygame.K_LEFT:
                    solider.MoovementLeft(GameField)
                elif event.key == pygame.K_RIGHT:
                    solider.MoovementRight(GameField)

print(GameField)