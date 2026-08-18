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
            screen.newScreen()
            time.sleep(1)
            state["pressed_enter"] = False
        screen.print_screen()
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
                solider.MoovementUP(game_field.Player_matrix)
            elif event.key == pygame.K_DOWN:
                solider.MoovementDown(game_field.Player_matrix)
            elif event.key == pygame.K_LEFT:
                solider.MoovementLeft(game_field.Player_matrix)
            elif event.key == pygame.K_RIGHT:
                solider.MoovementRight(game_field.Player_matrix)
            elif event.key == pygame.K_RETURN:
                state["pressed_enter"] = True

if __name__ == "__main__":
    main()