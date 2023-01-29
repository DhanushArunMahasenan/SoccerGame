import pygame

class SoccerBall:
	"""A class to manage the soccer ball."""

	def __init__(self, sg_game):
		"""Initialize soccer ball atrributes."""
		self.screen = sg_game.screen
		self.screen_rect = self.screen.get_rect()


		#Load the image of a soccer ball 
		self.image = pygame.image.load('images/soccer_ball.bmp')
		self.image_rect = self.screen_rect.center

	def blitbro(self):
		"""Draw soccer ball to screen."""
		self.screen.blit(self.image, self.image_rect)

	