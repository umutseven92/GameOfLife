﻿import pygame
import time
import sys
from grid import grid

# Colors used
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)

MARGIN = 5 # Margin between cells
WIDTH = 20 # Cell width
HEIGHT = 20 # Cell height
ROW = 40 # Random row count
COL = 40 # Random column count

speed_delta = 10 
max_speed = 125 
min_speed = 5
speed = min_speed

done = False
pause = False

pygame.init()



pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()


main = grid()

if len(sys.argv) > 1:
	main.load_map(sys.argv[1])
else:
	main.load_random(ROW, COL)

window_size = [WIDTH * len(main.grid[0]) + MARGIN * len(main.grid[0]) + MARGIN, HEIGHT * len(main.grid)+ MARGIN * len(main.grid) + MARGIN]
screen = pygame.display.set_mode(window_size)
screen.fill(gray)

def draw_grid():
	for row in range(len(main.grid)):
		for col in range(len(main.grid[row])):
			if main.grid[row][col] == 0:
				color = white 
			elif main.grid[row][col] == 1:
				color = black 
			pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# Quit
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				# Pause
				pause = not pause	
			elif event.key == pygame.K_r:
				# Reset
				if main.map_type == "random":
					main.load_random(ROW, COL)
				else:
					main.load_map(sys.argv[1])

				speed = min_speed
				if pause:
					pause = not pause
			elif event.key == pygame.K_ESCAPE:
				# Quit
				done = True
			elif event.key == pygame.K_RIGHT:
				# Speed up
				speed += speed_delta
				if speed > max_speed:
					speed = max_speed
			elif event.key == pygame.K_LEFT:
				# Speed down
				speed -= speed_delta
				if speed < min_speed:
					speed = min_speed

	if not pause:
		screen.fill(gray)

		draw_grid()

		main.apply_rules()

		clock.tick(speed)
		
		pygame.display.flip()

pygame.quit()
