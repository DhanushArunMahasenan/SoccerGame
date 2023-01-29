import pygame

class SoccerPlayer:
	"""A class to manage the soccer player."""

	def __init__(self, sg_game):
		"""Initialize soccer player attributes."""
		self.screen = sg_game.screen
		self.screen_rect = sg_game.screen.get_rect()

		#Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		#Load the image of the player
		self.image1 = pygame.image.load('images/soccer_player_1.bmp')
		self.rect1 = self.image1.get_rect()
		self.rect1.midleft = self.screen_rect.midleft
		

	def blityou(self):
		"""Draw the soccer player to its current position."""
		self.screen.blit(self.image1, self.rect1.midleft)
		
	
	def update(self):
		"""Update the soccer players's position based on the movement flag."""
		if self.moving_right and self.rect1.right <= self.screen_rect.right:
			self.rect1.x += 1
		if self.moving_left and self.rect1.left >= 0:
			self.rect1.x -= 1
		if self.moving_up and self.rect1.top >= self.screen_rect.top:
			self.rect1.y -= 1
		if self.moving_down and self.rect1.bottom <= self.screen_rect.bottom:
			self.rect1.y += 1
			

