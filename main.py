import pygame,time
import consts
import screen
import solider
import game_field


PlayerPos = pygame.Rect(0, 0, 50, 75)


def main():

    pygame.init()
    clock = pygame.time.Clock()
    while state["running"]:
        HandleInput()
        if state["pressed_enter"]:
            screen.newScreen(consts.SOLDIER_COL, consts.SOLDIER_ROW)
            time.sleep(1)
            state["pressed_enter"] = False

        screen.print_screen(consts.SOLDIER_COL,consts.SOLDIER_ROW )
    clock.tick(60)

state = {
    "MovementRight" : False,
    "MovementUp" : False,
    "MovementDown" : False,
    "MovementLeft" : False,
    "running": True,
    "pressed_enter": False,
}
def HandleInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_UP:
                solider.UP()
            elif event.key == pygame.K_DOWN:
                solider.Down()
            elif event.key == pygame.K_LEFT:
                solider.Left()
            elif event.key == pygame.K_RIGHT:
                solider.Right()
            elif event.key == pygame.K_RETURN:
                state["pressed_enter"] = True
    if solider.StopOnFlag(game_field.GameField, game_field.Player_matrix) == True:
        print("You Win!")
        state["running"] = False
    elif solider.StopOnTheMine(game_field.bomb_matrix, game_field.Player_matrix) == True:
        print("There is a bomb")
        screen.Bombaffect()

if __name__ == "__main__":
    main()