import pygame
import consts
import screen
import solider
import game_field

state = {
    "MoovementRight" : False,
    "MoovementUp" : False,
    "MoovementDown" : False,
    "MoovementLeft" : False,
    "running": True,
}
def main():
    pygame.init()
    clock = pygame.time.Clock()
    while state["running"]:
        HandleInput()
    clock.tick(60)

# for j in range(len(game_field.Player_matrix)):
#     for k in range(len(game_field.Player_matrix[j])):
#         if game_field.Player_matrix[j][k] == "_":
#             game_field.Player_matrix[j][k] = 0

PlayerPos = pygame.Rect(0, 0, 50, 75)


def HandleInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_UP:
                solider.MoovementUP(game_field.Player_matrix)
                print("1")
            elif event.key == pygame.K_DOWN:
                solider.MoovementDown(game_field.Player_matrix)
                print("2")
            elif event.key == pygame.K_LEFT:
                solider.MoovementLeft(game_field.Player_matrix)
                print("3")
            elif event.key == pygame.K_RIGHT:
                solider.MoovementRight(game_field.Player_matrix)
                print("4")
            elif event.key == pygame.K_RETURN:
                screen.show_screen = True
                print("5")


if __name__ == "__main__":
    main()