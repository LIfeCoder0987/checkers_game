from checkers_data import Checker_data

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
	white_moves = board_data.get_simple_player_moves(board_data.white)
	black_moves = board_data.get_simple_player_moves(board_data.black)
	print("len white_moves",len(white_moves))
	print("white_moves")
	for item in white_moves:
		print(item.from_row,item.from_col,item.to_row,item.to_col)
	print("len black_moves",len(black_moves))
	print("black_moves")
	for item in black_moves:
		print(item.from_row,item.from_col,item.to_row,item.to_col)