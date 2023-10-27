from Classes.GUIObjects.MenuClass import Menu, pygame

def setMenu(window, level, mode="pause"):
    paused = True
    menu = Menu()
    menuMode = mode
    pygame.mouse.set_visible(True)

    while paused:
        level.clock.tick(5)
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
                    level.restartLevel()
                    paused = False
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
                    menuMode = "exit"
            case "death":
                window.fill((35, 47, 75))
                menu.drawDeathMenu(window)
                if menu.yes_button.checkClick():
                    level.restartLevel()
                    paused = False
                elif menu.no_button.checkClick():
                    menuMode = "start"
            case "level_complete":
                window.fill((35, 47, 75))
                menu.drawLevelCompleteMenu(window)
                if menu.restart_button.checkClick():
                    level.restartLevel()
                    paused = False
                elif menu.quit_button.checkClick():
                    menuMode = "exit"

        pygame.display.update()
