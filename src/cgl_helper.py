from random import randint

def initial_grid(row, col):
	grid = []
	for row in range(row):
    		grid.append([])
    		for column in range(col):
        		grid[row].append(randint(0,1))  
	return grid

def get_neighbor_stat(grid, row, col, r, c):
	if row + r < 0 or row + r > len(grid) -1:
		return 0
	if col + c < 0 or col + c > len(grid[0]) -1:
		return 0

	if grid[row + r][col + c] == 1:
		return 1
	else:
	 	return 0

def apply_rules(grid, row, col):

	alive = get_alive_count(grid, row, col)
	cell = grid[row][col]

	if alive < 2 and cell == 1:
		grid[row][col] = 0
	elif alive > 3 and cell == 1:
		grid[row][col] = 0
	elif alive == 3 and cell == 0:
		grid[row][col] = 1
	
	return grid

def get_alive_count(grid, row, col):

	alive_count = 0
	
	alive_count += get_neighbor_stat(grid, row, col, 1, 0)
	alive_count += get_neighbor_stat(grid, row, col, 1, -1)
	alive_count += get_neighbor_stat(grid, row, col, 1, 1)
	alive_count += get_neighbor_stat(grid, row, col, 0, 1)
	alive_count += get_neighbor_stat(grid, row, col, -1, 1)
	alive_count += get_neighbor_stat(grid, row, col, 0, -1)
	alive_count += get_neighbor_stat(grid, row, col, -1, -1)
	alive_count += get_neighbor_stat(grid, row, col, -1, 0)

	return alive_count
