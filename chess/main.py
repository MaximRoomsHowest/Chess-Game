from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board

def run_tests():
	b = Board()
	print('\nInitial board:')
	b.print_board()

	try:
		# Test 1: Pawn moves forward one (BLACK pawn at a2 -> a3)
		pawn = b.get_piece('a2')
		print('\nTest: move pawn a2 -> a3')
		pawn.move()
		assert pawn.position == 'a3', f'Pawn position expected a3, got {pawn.position}'
		assert b.get_piece('a3') is pawn, 'Board did not update pawn position to a3'
		print('PASS: Pawn moved to a3')

		# Test 2: Rook moves forward one (BLACK rook a1 -> a2)
		rook = b.get_piece('a1')
		print('\nTest: move rook a1 forward 1 -> a2')
		rook.move('forward', 1)
		assert rook.position == 'a2', f'Rook position expected a2, got {rook.position}'
		assert b.get_piece('a2') is rook, 'Board did not update rook position to a2'
		print('PASS: Rook moved to a2')

		# Test 3: Bishop diagonal move (BLACK bishop c1 -> e3)
		bishop = b.get_piece('c1')
		print('\nTest: move bishop c1 forward-right 2 -> e3')
		bishop.move('forward-right', 2)
		assert bishop.position == 'e3', f'Bishop position expected e3, got {bishop.position}'
		assert b.get_piece('e3') is bishop, 'Board did not update bishop position to e3'
		print('PASS: Bishop moved to e3')

		# Test 4: Knight L-shape (BLACK knight g1 -> f3 via forward-left)
		knight = b.get_piece('g1')
		print('\nTest: move knight g1 forward-left (2 forward, 1 left) -> f3')
		knight.move('forward-left')
		assert knight.position == 'f3', f'Knight position expected f3, got {knight.position}'
		assert b.get_piece('f3') is knight, 'Board did not update knight position to f3'
		print('PASS: Knight moved to f3')

		print('\nAll tests passed.')

	except AssertionError as e:
		print('TEST FAILED:', e)


if __name__ == '__main__':
	run_tests()
