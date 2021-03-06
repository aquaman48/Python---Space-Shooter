import pygame

class Ship:
	"""A class class to manage the ship."""

	def __init__(self, ai_game):
		"""Initializes the ship and sets its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load('images/Ship.bmp')
		self.rect = self.image.get_rect()

		#Starts each new ship at the bottom of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		#store a decimal value for the ships horizontal postion.
		self.x = float(self.rect.x)

		#Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ships position based on movement flag"""
		#Update the ships x value not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#update rect object from self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)