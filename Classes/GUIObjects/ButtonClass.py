import pygame

IMAGE_PATH = 'Assets/MainObjects/GUI.png'
WIDTH, HEIGHT = 32, 16
START_X, START_Y = 112, 80
FONT = pygame.font.SysFont('Cybersomething', 30)
TEXT_COLOR = (229, 228, 226)

class Button(pygame.sprite.Sprite):
	def __init__(self, text):
		self.loadImage()
		self.rect = self.image.get_rect()
		self.button_name = self.createTextImage(text)
		self.button_name_position = pygame.math.Vector2()
		self.pressed_button_name_position = 0

	def checkClick(self):
		pos = pygame.mouse.get_pos()
		self.image = self.button_image
		self.pressed_button_name_position = 0

		if self.rect.collidepoint(pos):
			self.image = self.pressed_button_image
			self.pressed_button_name_position = 4
			if pygame.mouse.get_pressed()[0]:
				return True
			
	def draw(self, window, gap):
		self.rect.x = (window.get_width() - self.rect.width) // 2
		self.rect.y = (window.get_height() - self.rect.height) // 2 + gap
		window.blit(self.image, (self.rect.x, self.rect.y))
		window.blit(self.button_name, (self.rect.x + (self.rect.width - self.button_name.get_width()) // 2, self.rect.y + (self.rect.height - self.button_name.get_height()) // 2 + self.pressed_button_name_position))

	def loadImage(self):
		spritesheet = pygame.image.load(IMAGE_PATH)
		surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)

		rect = pygame.Rect(START_X, START_Y, WIDTH, HEIGHT)
		surface.blit(spritesheet, (0, 0), rect)
		self.button_image = pygame.transform.scale_by(surface, 4.5)
		self.image = self.button_image

		pressed_rect = pygame.Rect(START_X, START_Y + 16, WIDTH, HEIGHT)
		surface.blit(spritesheet, (0, 0), pressed_rect)
		self.pressed_button_image = pygame.transform.scale_by(surface, 4.5)

	def	createTextImage(self, text):
	    return FONT.render(text, True, TEXT_COLOR)
    