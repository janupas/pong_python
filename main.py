import pygame, sys
from pygame.locals import *

class Paddle:
	pass

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
	GREEN = pygame.Color(0, 255, 0)

	Clock = pygame.time.Clock()

	DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption(TITLE)
	
	# Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		Clock.tick(FPS)

def draw_paddle(px, py, pw, ph):
	return pygame.Rect(px, py, pw, ph)

if __name__ == '__main__':
	main()