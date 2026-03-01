class Board():
    def __init__(self):
        self.squares = self.create_board_dict()

    def create_board_dict(self):
        board = {}
        for row in range(ord('a'), ord('i')):
            for col in range(1, 9):
                square = f"{chr(row)}{col}"
                board[square] = None
        return board