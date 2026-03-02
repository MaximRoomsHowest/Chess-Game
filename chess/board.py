class Board():
    def __init__(self):
        self.squares = self.create_board_dict()
        # Place pieces on the board and let each piece know its board and position
        self.setup_board()

        # After setup_board has placed pieces into `self.squares`, inform each piece
        for square, piece in self.squares.items():
            if piece is not None:
                # set the piece's position to the board key and give it a reference to this board
                piece.set_initial_position(square)
                piece.define_board(self)

    def create_board_dict(self):
        board = {}
        for row in range(ord('a'), ord('i')):
            for col in range(1, 9):
                square = f"{chr(row)}{col}"
                board[square] = None
        return board
    
    def setup_board(self):
        from pieces import Rook, Knight, Bishop, Queen, King, Pawn
        # Black pieces
        self.squares['a1'] = Rook('BLACK', 1, "A1") # This defines the first Rook of the BLACK team.
        self.squares['b1'] = Knight('BLACK', 1, "B1") # This defines the first Knight of the BLACK team.
        self.squares['c1'] = Bishop('BLACK', 1, "C1") # This defines the first Bishop of the BLACK team.
        self.squares['d1'] = Queen('BLACK', 1, "D1") # This defines the first Queen of the BLACK team.
        self.squares['e1'] = King('BLACK', 1, "E1") # This defines the first King of the BLACK team.
        self.squares['f1'] = Bishop('BLACK', 2, "F1") # This defines the second Bishop of the BLACK team.
        self.squares['g1'] = Knight('BLACK', 2, "G1") # This defines the second Knight of the BLACK team.
        self.squares['h1'] = Rook('BLACK', 2, "H1") # This defines the second Rook of the BLACK team.

        # White pieces
        self.squares['a8'] = Rook('WHITE', 1, "A8") # This defines the first Rook of the WHITE team.
        self.squares['b8'] = Knight('WHITE', 1, "B8") # This defines the first Knight of the WHITE team.
        self.squares['c8'] = Bishop('WHITE', 1, "C8") # This defines the first Bishop of the WHITE team.
        self.squares['d8'] = Queen('WHITE', 1, "D8") # This defines the first Queen of the WHITE team.
        self.squares['e8'] = King('WHITE', 1, "E8") # This defines the first King of the WHITE team.
        self.squares['f8'] = Bishop('WHITE', 2, "F8") # This defines the second Bishop of the WHITE team.
        self.squares['g8'] = Knight('WHITE', 2, "G8") # This defines the second Knight of the WHITE team.
        self.squares['h8'] = Rook('WHITE', 2, "H8") # This defines the second Rook of the WHITE team.

        # Pawns
        for col in range(1, 9):
            self.squares[f"{chr(ord('a') + col - 1)}2"] = Pawn('BLACK', col, f"{chr(ord('a') + col - 1)}2") # This defines the Pawns of the BLACK team.
            self.squares[f"{chr(ord('a') + col - 1)}7"] = Pawn('WHITE', col, f"{chr(ord('a') + col - 1)}7") # This defines the Pawns of the WHITE team.
        

    def print_board(self):
        for row in range(1, 9):
            row_pieces = [str(self.squares[f"{chr(col)}{row}"]) if self.squares[f"{chr(col)}{row}"] else "Empty" for col in range(ord('a'), ord('i'))]
            print(f"{', '.join(row_pieces)}")

    def find_piece(self, symbol: str, identifier: int, color: str):
        for square, piece in self.squares.items():
            if piece and piece.symbol == symbol and piece.identifier == identifier and piece.color == color:
                return square
        return None
    
    def get_piece(self, square):
        """Returns the piece that is on a specific square"""
        return self.squares[square]

    def is_square_empty(self, square):
        """Returns True if the square is empty, False otherwise."""
        return self.get_piece(square) is None
    
    def kill_piece(self, square):
        """Removes a piece from the board by setting the square to None."""
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None