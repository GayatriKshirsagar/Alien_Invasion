import pygame
# Using sprite module, you can group related elements in your game and act on all grouped elements at once
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""This line declares the Bullet class as a subclass of Sprite."""
	"""Create a bullet object at the ship's current position."""
	#  super().__init__() ensures that the Bullet class is properly initialized as a Sprite.
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color


		# Create a bullet rect at (0, 0) and then set the correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# update the decimal poistion of the bullet
		self.y -= self.settings.bullet_speed
		# Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		#  Pygame function that draws a rectangle on the screen.
		pygame.draw.rect(self.screen, self.color, self.rect)