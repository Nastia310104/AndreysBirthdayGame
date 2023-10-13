from Classes.GUIObjects.MenuClass import Menu, pygame

def setMenu(window, clock, mode="pause"):
    paused = True
    menu = Menu()
    menuMode = mode

    while paused:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

        match menuMode:
            case "pause":
                window.fill((35, 47, 75))
                menu.drawPauseMenu(window)
                if menu.resume_button.checkClick():
                    paused = False
                elif menu.quit_button.checkClick():
                    menuMode = "exit"
                elif menu.restart_button.checkClick():
                    return
            case "exit":
                window.fill((35, 47, 75))
                menu.drawExitMenu(window)
                if menu.no_button.checkClick():
                    menuMode = "pause"
                elif menu.yes_button.checkClick():
                    pygame.quit()
                    quit()
            case "start":
                window.fill((35, 47, 75))
                menu.drawStartMenu(window)
                if menu.start_button.checkClick():
                    return True
                elif menu.quit_button.checkClick():
                    pygame.quit()
                    quit()
            case "death":
                window.fill((35, 47, 75))
                menu.drawDeathMenu(window)
                if menu.yes_button.checkClick():
                    return
                elif menu.no_button.checkClick():
                    menuMode = "start"
            # TODO: add level reset
        pygame.display.update()
