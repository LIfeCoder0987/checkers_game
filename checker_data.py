import numpy as np 
from checkers_move import Checkers_move

class Checker_data:
	def __init__(self, rows=8, cols=8):
		self.rows = rows
		self.cols = cols
		self._range = [i for i in range(0,8)]
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
		self.board[1,3] = self.white_king
		self.board[7,3] = self.black_king

	def get_pieces_position(self):
		dict_pos = {
					self.white:[],self.black:[],
					self.white_king:[],self.black_king:[]
					}
		for row in range(self.rows):
			for col in range(self.cols):
				if self.board[row,col] == self.white:
					dict_pos[self.white].append((row,col))
				if self.board[row,col] == self.black:
					dict_pos[self.black].append((row,col))
				if self.board[row,col] == self.white_king:
					dict_pos[self.white_king].append((row,col))
				if self.board[row,col] == self.black_king:
					dict_pos[self.black_king].append((row,col))

		return dict_pos

	def get_moves(self):
		moves = []

		dict_pos = self.get_pieces_position()

		for piece in dict_pos.keys():

			if piece == self.white:
				white_pos = dict_pos[piece]
				for row,col in white_pos:
					if self.can_jump(piece,row,col,row-1,col+1,row-2,col+2):
						moves.append(Checkers_move(row,col,row-2,col+2))
					if self.can_jump(piece,row,col,row-1,col-1,row-2,col-2):
						moves.append(Checkers_move(row,col,row-2,col-2))

			if piece == self.black:
				black_pos = dict_pos[piece]
				for row,col in black_pos:
					if self.can_jump(piece,row,col,row+1,col+1,row+2,col+2):
						moves.append(Checkers_move(row,col,row+2,col+2))
					if self.can_jump(piece,row,col,row+1,col-1,row+2,col-2):
						moves.append(Checkers_move(row,col,row+2,col-2))

			if piece == self.white_king:
				pass

			if piece == self.black_king:
				pass

		if len(moves)==0:
			for piece in dict_pos.keys():

				if piece == self.white:
					white_pos = dict_pos[piece]
					for row, col in white_pos:
						if self.can_move(piece,row,col,row-1,col-1):
							moves.append(Checkers_move(row,col,row-1,col-1))
						if self.can_move(piece,row,col,row-1,col+1):
							moves.append(Checkers_move(row,col,row-1,col+1))

				if piece == self.black:
					black_pos = dict_pos[piece]
					for row, col in black_pos:
						if self.can_move(piece,row,col,row+1,col-1):
							moves.append(Checkers_move(row,col,row+1,col-1))
						if self.can_move(piece,row,col,row+1,col+1):
							moves.append(Checkers_move(row,col,row+1,col+1))

				if piece == self.white_king:
					white_king_pos = dict_pos[piece]
					for row, col in white_king_pos:
						checker_move_list = self.can_move(piece,row,col,0,0)
						for i in checker_move_list:
							moves.append(i)

				if piece == self.black_king:
					pass

		return moves

	def can_move(self,piece,row1,col1,row2,col2):

		if piece == self.white:
			if col>-1 and col<8 and self.board[row2,col2] == self.empty:
				return True
			return False

		if piece == self.black:
			if col>-1 and col<8 and self.board[row2,col2] == self.empty:
				return True
			return False

		if piece == self.white_king:
			checker_move_list = []
			rows = self._range[row1+1:]
			r_rows = self._range[row1-1::-1]
			cols = self._range[col1+1:]
			r_cols = self._range[col1-1::-1]
			if len(rows)>len(cols):
				for col_2 in cols:
					row_2 = rows[cols.index(col_2)]
					checker_move_list.append(Checkers_move(row1,col1,row_2,col_2))
				for row_2 in r_rows:
					col_2 = r_cols[r_rows.index(row_2)]
					checker_move_list.append(Checkers_move(row1,col1,row_2,col_2))
			elif len(rows)<len(cols):
				pass
			elif len(rows)==len(cols):
				pass

			return checker_move_list

		if piece == self.black_king:
			pass

	def can_jump(self,piece,row1,col1,row2,col2,row3,col3):

		if piece == self.white:
			if col2>-1 and col2<8\
			and self.board[row2,col2] == self.black\
			and self.board[row3,col3] == self.empty:
				return True
			return False

		if piece == self.black:
			if col2>-1 and col2<8\
			and self.board[row2,col2] == self.white\
			and self.board[row3,col3] == self.empty:
				return True
			return False

		if piece == self.white_king:
			pass
		if piece == self.black_king:
			pass