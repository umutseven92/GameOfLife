import pygame
import cgl_helper
import time

# Colors used
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)

MARGIN = 5 # Margin between cells
WIDTH = 20 # Cell width
HEIGHT = 20 # Cell height
ROW = 40 # Row count
COL = 40 # Column count

speed_delta = 10 
max_speed = 120 
min_speed = 10
speed = min_speed

done = False
pause = False

pygame.init()

window_size = [WIDTH * COL + MARGIN * COL + MARGIN, HEIGHT * ROW + MARGIN * ROW + MARGIN]

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

screen.fill(gray)
grid = cgl_helper.initial_grid(ROW, COL)

def draw_grid():
	for row in range(ROW):
		for col in range(COL):
			if grid[row][col] == 0:
				color = white 
			elif grid[row][col] == 1:
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
				grid = cgl_helper.initial_grid(ROW, COL)
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

		for row in range(ROW):
			for col in range(COL):
				grid = cgl_helper.apply_rules(grid, row, col)

		clock.tick(speed)
		
		pygame.display.flip()

pygame.quit()


