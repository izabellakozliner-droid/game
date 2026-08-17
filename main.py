import pygame
import consts
import solider
import game_field

SystemRun = True
# matrix = game_field.CreateGameField(25, 50)
# game_field.FlagSpawn(matrix)
# solider.StartSoldierPos(matrix)
# game_field.MinesGenerator(matrix)

# for col in zip(matrix):
#     print(list(col))


playerChar = pygame.Rect(0, 0, 60, 80)


def HandleInput(events):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                SystemRun = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    solider.MoovementUP(game_field.player_matrix)
                elif event.key == pygame.K_DOWN:
                    solider.MoovementDown(game_field.player_matrix)
                elif event.key == pygame.K_LEFT:
                    solider.MoovementLeft(game_field.player_matrix)
                elif event.key == pygame.K_RIGHT:
                    solider.MoovementRight(game_field.player_matrix)
