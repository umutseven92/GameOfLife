from random import randint
import pdb

class grid:
	def load_map(self, data):
		with open(data, "r") as file:
			loaded = file.readlines()
		self.desc = ""
		cell = []
		max_length = 0

		for i in range(0, len(loaded)):
			if loaded[i].startswith("#D"):
				# Description
				self.desc +="\n" + loaded[i]
			elif loaded[i].startswith("#N"):
				# Classic rules
				self.rules = "classic"
			elif loaded[i].startswith("#P"):
				# Position
				self.pos = loaded[i]
			elif loaded[i].startswith("#"):
				# Name
				self.name = loaded[i]
			elif loaded[i].startswith(".") or loaded[i].startswith("*"):
				# Grid
				length = len(loaded[i])-1
				if length > max_length:
					max_length = length

				row = []
				for k in range(0, len(loaded[i])):
					if loaded[i][k] == "*":
						row.append(1)
					elif loaded[i][k] == ".":
						row.append(0)

				cell.append(row)
			
		for i in range(len(cell)):
			for k in range(max_length - len(cell[i])):
				cell[i].append(0)

		self.grid = cell
		self.map_type = "user"

	def load_random(self, row, col):

		self.name = "Random grid"
		self.desc = "Randomly generated grid"
		self.rules = "classic"
		self.pos = ""
		self.map_type = "random"

		cell = []
		for row in range(row):
			cell.append([])
			for column in range(col):
				cell[row].append(randint(0,1))

		self.grid = cell
		
	def apply_rules(self):
		cells_to_delete = []	
		cells_to_reanimate = []	

		for row in range(len(self.grid)):
			for col in range(len(self.grid[row])):
				
				alive = self.get_alive_count(row, col)
				cell = self.grid[row][col]

				if alive < 2 and cell == 1:
					cells_to_delete.append([row, col])
				elif alive > 3 and cell == 1:
					cells_to_delete.append([row, col])
				elif alive == 3 and cell == 0:
					cells_to_reanimate.append([row,col])

		for i in range(len(cells_to_delete)):
			el = cells_to_delete[i]
			self.grid[el[0]][el[1]] = 0

		for i in range(len(cells_to_reanimate)):
			el = cells_to_reanimate[i]
			self.grid[el[0]][el[1]] = 1

	def get_alive_count(self,row, col):

		alive_count = 0
			
		# South
		alive_count += self.get_neighbor_stat(row, col, 1, 0)
		# Southwest 
		alive_count += self.get_neighbor_stat(row, col, 1, -1)
		# Southeast
		alive_count += self.get_neighbor_stat(row, col, 1, 1)
		# East
		alive_count += self.get_neighbor_stat(row, col, 0, 1)
		# Northeast
		alive_count += self.get_neighbor_stat(row, col, -1, 1)
		# West
		alive_count += self.get_neighbor_stat(row, col, 0, -1)
		# Northwest
		alive_count += self.get_neighbor_stat(row, col, -1, -1)
		# North
		alive_count += self.get_neighbor_stat(row, col, -1, 0)

		return alive_count
	
	def get_neighbor_stat(self, row, col, r, c):

		n_row = row + r
		n_col = col + c

		if n_row < 0 or n_row > len(self.grid) -1:
			return 0
		if n_col < 0 or n_col > len(self.grid[0]) -1:
			return 0

		if self.grid[n_row][n_col] == 1:
			return 1
		else:
			return 0
