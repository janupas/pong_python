import pygame, sys
from pygame.locals import *

class Paddle:
	# Uniform Velocity of the paddle
	pV = 20

	def __init__(self, surface, color, px, py, pw, ph):
		self.surface = surface
		self.color = color
		self.px = px
		self.py = py
		self.pw = pw
		self.ph = ph

	def draw(self):
		pygame.draw.rect(self.surface, self.color, pygame.Rect(self.px, self.py, self.pw, self.ph))

def main():
	pygame.init()

	# Constansts
	FPS = 60
	TITLE = 'Ping-Pong'
	WINDOW_WIDTH = 1000
	WINDOW_HEIGHT = 800
	PADDLE_WIDTH = 20
	PADDLE_HEIGHT = 150

	# Colors
	BLACK = pygame.Color(0, 0, 0)
	WHITE = pygame.Color(255, 255, 255)
	GREEN = pygame.Color(0, 255, 0)

	Clock = pygame.time.Clock()

	DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption(TITLE)

	left_paddle = Paddle(DISPLAY, WHITE, 0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
	right_paddle = Paddle(DISPLAY, WHITE, WINDOW_WIDTH - PADDLE_WIDTH, 0, PADDLE_WIDTH, PADDLE_HEIGHT)

	# Line in the middle of the screen

	# Main game loop
	while True:
		# Clearing surface before frame render
		DISPLAY.fill(BLACK)
		pygame.draw.line(DISPLAY, WHITE, (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 1)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYDOWN:
				if event.key == pygame.K_UP:
					# Right paddle up
					right_paddle.py -= Paddle.pV

				if event.key == pygame.K_DOWN:
					# Right paddle down
					right_paddle.py += Paddle.pV

				if event.key == pygame.K_w:
					# Left paddle up
					left_paddle.py -= Paddle.pV

				if event.key == pygame.K_s:
					# Left paddle down
					left_paddle.py += Paddle.pV
		
		left_paddle.draw()
		right_paddle.draw()

		pygame.display.update()
		Clock.tick(FPS)

if __name__ == '__main__':
	main()