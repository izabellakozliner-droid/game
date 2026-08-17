import pygame,time
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
    "pressed_enter": False,
}

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



def HandleInput():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #solider.MoovementUP(matrix)
                    print("")
                elif event.key == pygame.K_DOWN:
                    #solider.MoovementDown(matrix)
                    print("")
                elif event.key == pygame.K_LEFT:
                    #solider.MoovementLeft(matrix)
                    print("")
                elif event.key == pygame.K_RIGHT:
                    #solider.MoovementRight(matrix)
                    print("")
                if event.key == pygame.K_RETURN:
                    state["pressed_enter"] = True
                    print("")


if __name__ == "__main__":
    main()