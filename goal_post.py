import pygame

class GoalPost:
	"""A class to manage the goal post."""

	def __init__(self, sg_game):
		"""Initialize goal post attributes."""
		self.screen = sg_game.screen
		self.screen_rect = self.screen.get_rect()

		#Load the goal post image
		self.image1 = pygame.image.load('images/goal_post.bmp')
		self.image2 = pygame.image.load('images/goal_post_2.bmp')
		self.rect_1 = self.image1.get_rect()
		self.rect_2 = self.image2.get_rect()
		
		#The goal post should be at the bottom of the screen
		self.rect_1.midtop = self.screen_rect.midtop
		self.rect_2.midbottom = self.screen_rect.midbottom
	
	def blitme(self):
		"""Draw the goal to its current location."""
		self.screen.blit(self.image1, self.rect_1)
		self.screen.blit(self.image2, self.rect_2)