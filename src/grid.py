from random import randint
import pdb

class grid:
	def load_map(self, data):
		with open("D:/Projects/gameoflife/maps/blinker_105.lif", "r") as file:
			loaded = file.readlines()

		self.desc = ""
		cell = []
		j = 0
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
			else:
				# Grid
				row = []
				self.col = len(loaded[i]) -1
				for k in range(0, len(loaded[i])):
					if loaded[i][k] == "*":
						row.append(1)
					elif loaded[i][k] == ".":
						row.append(0)
				cell.append(row)
				self.row = len(cell)
				j+=1

		self.grid = cell

	def load_random(self, row, col):

		self.name = "Random grid"
		self.desc = "Randomly generated grid"
		self.rules = "classic"
		self.pos = ""
		self.row = row
		self.col = col

		cell = []
		for row in range(row):
			cell.append([])
			for column in range(col):
				cell[row].append(randint(0,1))

		self.grid = cell
		
	def apply_rules(self):
		for row in range(self.row):
			for col in range(self.col):
			
				alive = self.get_alive_count(row, col)
				cell = self.grid[row][col]

				#pdb.set_trace()
				print alive,
					
				if alive < 2 and cell == 1:
					self.grid[row][col] = 0
				elif alive > 3 and cell == 1:
					self.grid[row][col] = 0
				elif alive == 3 and cell == 0:
					self.grid[row][col] = 1

	def get_alive_count(self,row, col):

		alive_count = 0
		
		alive_count += self.get_neighbor_stat(row, col, 1, 0)
		alive_count += self.get_neighbor_stat(row, col, 1, -1)
		alive_count += self.get_neighbor_stat(row, col, 1, 1)
		alive_count += self.get_neighbor_stat(row, col, 0, 1)
		alive_count += self.get_neighbor_stat(row, col, -1, 1)
		alive_count += self.get_neighbor_stat(row, col, 0, -1)
		alive_count += self.get_neighbor_stat(row, col, -1, -1)
		alive_count += self.get_neighbor_stat(row, col, -1, 0)

		return alive_count
	
	def get_neighbor_stat(self, row, col, r, c):

		if row + r < 0 or row + r > len(self.grid) -1:
			return 0
		if col + c < 0 or col + c > len(self.grid[0]) -1:
			return 0

		if self.grid[row + r][col + c] == 1:
			return 1
		else:
			return 0
