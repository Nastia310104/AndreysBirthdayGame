import pygame
from Classes.LevelObjects.LevelObjectClass import LevelObject

FONT = pygame.font.SysFont('Cybersomething', 30)
TEXT_COLOR = (50, 50, 50)

IMAGE_PATH = 'Assets/MainObjects/Item1.png'

TEXT_EXAMPLE = 'Hi! This is example text to check how does shit work :)'

POPUP_GROUP = pygame.sprite.Group()

class PopUp(LevelObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 881
        self.height = 620
        self.loadSprites(IMAGE_PATH, 0.2)
        self.rect = self.image.get_rect()
        self.counter = 0
        self.show = False

    def blitText(self, window, dx, dy, text):
        text_image = FONT.render(text, True, TEXT_COLOR)
        window.blit(text_image, (dx + (self.rect.width - text_image.get_width()) // 2, dy + (self.rect.height - self.rect.height * 0.25 - text_image.get_height()) // 2))

    def draw(self, window, dx, dy):
        super().draw(window, dx, dy)
        self.blitText(window, dx, dy, TEXT_EXAMPLE)

    def deletePopUp(self):
        self.kill()

        # TODO: text position recount
        # Player touch trigger -> Pop Up class checks counter -> Load image or text (if overkilling) -> Pop Up shows and stand 'till player press Enter -> Pop Up's counter do += 1 
        # Maybe it's better to draw text? well, I need + and - of each approach