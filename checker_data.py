import numpy as np 
from checkers_move import Checkers_move

class Checker_data:
	def __init__(self, rows=8, cols=8):
		self.rows = rows
		self.cols = cols
		self.empty = 0
		self.white = 1
		self.black = 2
		self.white_king = 3
		self.black_king = 4
		self.init_board()

	def init_board(self):
		self.board = np.zeros((self.rows, self.cols))
		# for row in range(self.rows):
		# 	for col in range(self.cols):
		# 		if row%2 == col%2:
		# 			if row<3:
		# 				self.board[row,col] = self.black
		# 			elif row>4:
		# 				self.board[row,col] = self.white
		# 			else:
		# 				self.board[row,col] = self.empty
		# 		else:
		# 			self.board[row,col] = self.empty
		self.board[5,1] = self.white
		self.board[4,0] = self.black


	def get_simple_player_moves(self, simple_player):
		moves = []

		"""simple_position is a list of (row,col) tuple of the specific player"""
		simple_position = self.get_simpte_position(simple_player)

		"""we iterate through the postion and unpacking the (row,col) tuple"""
		for row,col in simple_position:

			"""checking if the simple_player paramater is the white player"""
			if simple_player == self.white:
				"""checking the left side"""
				if self.board[row-1,col-1] == self.black:
					"""checking if the moves will be out of the board"""
					if col-2>=0:
						"""appending the jump move"""
						moves.append(CheckersMove(row,col,row-2,col-2))
				"""checking the right side"""
				if self.board[row-1,col+1] == self.black:
					"""checking if the moves will be out of the board"""
					if col+2<=7:
						"""appending the jump move"""
						moves.append(CheckersMove(row,col, row-2, col+2))

			"""checking if the function recieved a black player parameter"""
			elif simple_player == self.black:
				"""checking the left side"""
				if self.board[row+1,col-1] == self.white:
					"""checking if the move is out of the board"""
					if col-2>=0:
						"""appending the jump move"""
						moves.append(CheckersMove(row,col,row+2,col-2))
				"""checking the right side"""
				if self.board[row+1,col+1] == self.white:
					"""checking if the move will be out of the board"""
					if col+2<=7:
						"""appending the jump move"""
						moves.append(CheckersMove(row,col,row+2,col+2))

		"""we want the jump to be the only moves avaleble because the jump is a must
			move"""
		if len(moves)==0:
			"""other wise we continue to check for normale moves"""
			for row,col in simple_position:
				"""if the passed paramater of the player is the white player"""
				if simple_player == self.white:
					"""checking if the move will be out the board the left side
						we want the col to be always smoll than zero so we can move"""
					if col-1>=0:
						"""checking if the next place is empty"""
						if self.board[row-1,col-1] == self.empty:
							"""append the normale move"""
							moves.append(CheckersMove(row, col, row-1, col-1))
					"""checking if the moves will be out the board the right side"""
					if col+1<=7:
						"""checking if the next place is empty"""
						if self.board[row-1,col+1] == self.empty:
							"""appending the move"""
							moves.append(CheckersMove(row, col, row-1, col+1))
				"""if the passed paramater of the player is the black player"""
				elif simple_player == self.black:
					"""checking if the move will be out of the board"""
					if col-1>=0:
						"""the next place must be empty"""
						if self.board[row+1,col-1] == self.empty:
							"""appending the move"""
							moves.append(CheckersMove(row, col, row+1, col-1))
					"""checking if the move will be out of the board"""
					if col+1<=7:
						"""the next place must be empty"""
						if self.board[row+1,col+1] == self.empty:
							"""appending the move"""
							moves.append(CheckersMove(row, col, row+1, col+1))
		return moves

	def get_simpte_position(self, player):
		"""function that iterate through the board and return a list of tuples (row,col)
			of the specific player"""
		simple_position = []
		for row in range(self.rows):
			for col in range(self.cols):
				if self.board[row,col] == player:
					simple_position.append((row,col))
		return simple_position