
import sys

import pygame
from settings import Settings
from goal_post import GoalPost
from soccer_player import SoccerPlayer
from soccer_ball import SoccerBall

class SoccerGame:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize game, and game attributes."""
		pygame.init()
		
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Soccer Game")

		self.goal = GoalPost(self)
		self.soccer_player = SoccerPlayer(self)
		self.soccer_ball = SoccerBall(self)

	def collision_ball_player(self):
		#Detect a collision and move the ball 2 pixels.
		if self.soccer_player.rect1.colliderect(self.soccer_ball.image_rect):
			self.soccer_ball.image_rect += 5 


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.soccer_player.update()
			self._update_screen()
			self.collision_ball_player()
	
	def _check_events(self):
		"""Respond to keypress and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.soccer_player.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.soccer_player.moving_left = True
				if event.key == pygame.K_UP:
					self.soccer_player.moving_up = True
				elif event.key == pygame.K_DOWN:
					self.soccer_player.moving_down = True
			
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.soccer_player.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.soccer_player.moving_left = False
				if event.key == pygame.K_UP:
					self.soccer_player.moving_up = False
				elif event.key == pygame.K_DOWN:
					self.soccer_player.moving_down = False
					

	def _update_screen(self):
		"""Update images on screen, and flip to new screen."""
			#Redraw screen through each pass through the loop.
		self.screen.fill(self.settings.bg_color)
		self.goal.blitme()
		self.soccer_player.blityou()
		self.soccer_ball.blitbro()
		#Make the most recently drawn screen visible
		pygame.display.flip()

	


if __name__ == '__main__':
	sg = SoccerGame()
	sg.run_game()