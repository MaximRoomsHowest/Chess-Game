from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board

new_board = Board()
print(new_board.squares)
new_pawn = Pawn("BLACK", 1)
new_pawn.move()

