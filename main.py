from checker_data import Checker_data

def print_board(b):
	print("    0   1   2   3   4   5   6   7")
	for row in range(b.rows):
		print("  ---------------------------------")
		for col in range(b.cols):
			if col==0:
				print(str(row)+" |",end="")
			if b.board[row,col] == b.black:
				print(" B |", end="")
			elif b.board[row,col] == b.black_king:
				print(" BK|", end="")
			elif b.board[row,col] == b.white:
				print(" W |", end="")
			elif b.board[row,col] == b.white_king:
				print(" WK|", end="")
			elif b.board[row,col] == b.empty:
				print("   |", end="")
		print("")

if __name__ == '__main__':

	board_data = Checker_data()
	print_board(board_data)
	moves = board_data.get_moves()
	print(len(moves))
	for move in moves:
		print(move.from_row,move.from_col,move.to_row,move.to_col)
	# pieces_position = board_data.get_pieces_position()
	# for piece in pieces_position.keys():
	# 	if piece == board_data.white:
	# 		print("white piece(s) at",pieces_position[piece])
	# 	if piece == board_data.black:
	# 		print("black piece(s) at",pieces_position[piece])
	# 	if piece == board_data.white_king:
	# 		print("white king piece(s) at", pieces_position[piece])
	# 	if piece == board_data.black_king:
	# 		print("black king piece(s) at", pieces_position[piece])
