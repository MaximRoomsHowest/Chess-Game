from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board

new_board = Board()
new_board.setup_board()
new_board.print_board()
new_pawn = Pawn("BLACK", 1)
new_pawn.move()

