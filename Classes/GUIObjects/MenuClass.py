import pygame
from Classes.GUIObjects.ButtonClass import Button

MENU_IMAGE = 'Assets/MainObjects/menu.png'
WIDTH, HEIGHT = 48, 64
BUTTON_GAP = HEIGHT // 4 * 4.5
FONT = pygame.font.SysFont('Cybersomething', 30)
TEXT_COLOR = (229, 228, 226)

class Menu(pygame.sprite.Sprite):
	def __init__(self):
		self.loadButtons()
		self.loadImage()
		self.rect = self.image.get_rect()

	def draw(self, window, text):
		self.createTextImage(text)
		window.blit(self.image, ((window.get_width() - self.rect.width) // 2, (window.get_height() - self.rect.height) // 2))
		window.blit(self.text, ((window.get_width() - self.text.get_width()) // 2, (window.get_height() - self.text.get_height()) // 2 - self.rect.height // 2 - self.text.get_height()))

	def drawPauseMenu(self, window):
		self.draw(window, 'Pause')
		self.resume_button.draw(window, BUTTON_GAP * -1)
		self.restart_button.draw(window, 0)
		self.quit_button.draw(window, BUTTON_GAP)

	def drawExitMenu(self, window):
		self.draw(window, 'Are you sure?')
		self.yes_button.draw(window, BUTTON_GAP * 0.7 * -1)
		self.no_button.draw(window, BUTTON_GAP * 0.7)

	def drawStartMenu(self, window):
		self.draw(window, 'Let\'s start!')
		self.start_button.draw(window, BUTTON_GAP * 0.7 * -1)
		self.quit_button.draw(window, BUTTON_GAP * 0.7)

	def	drawDeathMenu(self, window):
		self.draw(window, 'Start again?')
		self.yes_button.draw(window, BUTTON_GAP * 0.7 * -1)
		self.no_button.draw(window, BUTTON_GAP * 0.7)
  
	def drawLevelCompleteMenu(self, window):
		self.draw(window, "Level complete. Congrats!")
		self.restart_button.draw(window, BUTTON_GAP * 0.7 * -1)
		self.quit_button.draw(window, BUTTON_GAP * 0.7)

	def loadImage(self):
		spritesheet = pygame.image.load(MENU_IMAGE)
		surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
		rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
		surface.blit(spritesheet, (0, 0), rect)
		self.image = pygame.transform.scale_by(surface, 4.5)

	def loadButtons(self):		
		self.resume_button = Button('Resume')
		self.quit_button = Button('Quit')
		self.start_button = Button('Start')
		self.restart_button = Button('Restart')
		self.yes_button = Button('Yes')
		self.no_button = Button('No')

	def	createTextImage(self, text):
	    self.text = FONT.render(text, True, TEXT_COLOR)



	