from abc import abstractmethod, ABC
from chess.BoardMovement import BoardMovement

class BaseChessPiece(ABC):
    def __init__(self, color, name, symbol, identifier, position):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = position
        # Will be filled by the Board after setup
        self.board = None
        self.is_alive = True

    def set_initial_position(self, square: str):
        """Set the piece's position from the board key (called by Board)."""
        # normalize to lowercase board keys
        self.position = square.lower()

    def define_board(self, board):
        """Provide a reference to the Board instance this piece lives on."""
        self.board = board

    @abstractmethod
    def move(self, movement):
        """Move this piece to a new square. `movement` is the target square (or None).

        If the piece has a `board` reference, update the board's `squares` mapping
        and the piece's own `position`. If `movement` is None, do nothing.
        """
        # Default implementation: if movement is None, print and return
        if movement is None:
            print(None)
            return None

        # If no board is defined, just print the movement (fallback)
        if not hasattr(self, 'board') or self.board is None:
            print(movement)
            # still update own position
            self.position = movement.lower()
            return movement.lower()

        old_pos = self.position.lower()
        new_pos = movement.lower()

        # Validate positions exist on the board
        if old_pos not in self.board.squares or new_pos not in self.board.squares:
            # fallback: print movement and set position
            print(movement)
            self.position = new_pos
            return new_pos

        # Capture if a piece exists on the destination
        dest_piece = self.board.get_piece(new_pos)
        if dest_piece is not None:
            dest_piece.die()

        # Move the piece on the board dictionary
        self.board.squares[new_pos] = self
        self.board.squares[old_pos] = None
        self.position = new_pos

        # Return the new position
        print(new_pos)
        return new_pos

    @abstractmethod
    def die(self):
        pass

class Pawn(BaseChessPiece):
    def __init__(self, color, identifier, position):
        super().__init__(color, 'Pawn', '-', identifier, position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        # Pawn moves one square forward (direction depends on color)
        movement = BoardMovement.forward(self.position, self.color, 1)
        super().move(movement)

    def die(self):
        self.is_alive = False

class Rook(BaseChessPiece):
    def __init__(self, color, identifier, position):
        super().__init__(color, 'Rook', 'R', identifier, position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self, direction: str, squares: int = 1):
        # Rook moves straight in one of the four cardinal directions
        d = direction.lower()
        if d == 'left':
            movement = BoardMovement.left(self.position, squares)
        elif d == 'right':
            movement = BoardMovement.right(self.position, squares)
        elif d == 'forward':
            movement = BoardMovement.forward(self.position, self.color, squares)
        elif d == 'backward':
            movement = BoardMovement.backward(self.position, self.color, squares)
        else:
            raise ValueError(f"Unknown direction for Rook: {direction}")

        super().move(movement)

    def die(self):
        self.is_alive = False

class Bishop(BaseChessPiece):
    def __init__(self, color, identifier, position):
        super().__init__(color, 'Bishop', 'B', identifier, position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self, direction: str, squares: int = 1):
        # Bishop moves diagonally in four directions
        d = direction.lower()
        if d == 'forward-left':
            movement = BoardMovement.forward_left(self.position, self.color, squares)
        elif d == 'forward-right':
            movement = BoardMovement.forward_right(self.position, self.color, squares)
        elif d == 'backward-left':
            movement = BoardMovement.backward_left(self.position, self.color, squares)
        elif d == 'backward-right':
            movement = BoardMovement.backward_right(self.position, self.color, squares)
        else:
            raise ValueError(f"Unknown direction for Bishop: {direction}")

        super().move(movement)

    def die(self):
        self.is_alive = False

class Knight(BaseChessPiece):
    def __init__(self, color, identifier, position):
        super().__init__(color, 'Knight', 'N', identifier, position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self, direction: str):
        # Knight moves in an L-shape. There are two variants for each diagonal-like direction:
        # - 'forward-left' means 2 forward and 1 left
        # - 'left-forward' means 1 forward and 2 left
        d = direction.lower()

        def try_chain(first_move, second_move):
            if first_move is None:
                return None
            return second_move(first_move)

        movement = None
        if d == 'forward-left':
            p = BoardMovement.forward(self.position, self.color, 2)
            movement = try_chain(p, lambda pos: BoardMovement.left(pos, 1) if pos else None)
        elif d == 'left-forward':
            p = BoardMovement.left(self.position, 2)
            movement = try_chain(p, lambda pos: BoardMovement.forward(pos, self.color, 1) if pos else None)
        elif d == 'forward-right':
            p = BoardMovement.forward(self.position, self.color, 2)
            movement = try_chain(p, lambda pos: BoardMovement.right(pos, 1) if pos else None)
        elif d == 'right-forward':
            p = BoardMovement.right(self.position, 2)
            movement = try_chain(p, lambda pos: BoardMovement.forward(pos, self.color, 1) if pos else None)
        elif d == 'backward-left':
            p = BoardMovement.backward(self.position, self.color, 2)
            movement = try_chain(p, lambda pos: BoardMovement.left(pos, 1) if pos else None)
        elif d == 'left-backward':
            p = BoardMovement.left(self.position, 2)
            movement = try_chain(p, lambda pos: BoardMovement.backward(pos, self.color, 1) if pos else None)
        elif d == 'backward-right':
            p = BoardMovement.backward(self.position, self.color, 2)
            movement = try_chain(p, lambda pos: BoardMovement.right(pos, 1) if pos else None)
        elif d == 'right-backward':
            p = BoardMovement.right(self.position, 2)
            movement = try_chain(p, lambda pos: BoardMovement.backward(pos, self.color, 1) if pos else None)
        else:
            raise ValueError(f"Unknown direction for Knight: {direction}")

        super().move(movement)

    def die(self):
        self.is_alive = False

class Queen(BaseChessPiece):
    def __init__(self, color, identifier, position):
        super().__init__(color, 'Queen', 'Q', identifier, position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self, direction: str, squares: int = 1):
        # Queen can move like Rook or Bishop
        d = direction.lower()
        if d in ('left', 'right', 'forward', 'backward'):
            # reuse Rook-like movement
            if d == 'left':
                movement = BoardMovement.left(self.position, squares)
            elif d == 'right':
                movement = BoardMovement.right(self.position, squares)
            elif d == 'forward':
                movement = BoardMovement.forward(self.position, self.color, squares)
            else:
                movement = BoardMovement.backward(self.position, self.color, squares)
        else:
            # diagonal
            if d == 'forward-left':
                movement = BoardMovement.forward_left(self.position, self.color, squares)
            elif d == 'forward-right':
                movement = BoardMovement.forward_right(self.position, self.color, squares)
            elif d == 'backward-left':
                movement = BoardMovement.backward_left(self.position, self.color, squares)
            elif d == 'backward-right':
                movement = BoardMovement.backward_right(self.position, self.color, squares)
            else:
                raise ValueError(f"Unknown direction for Queen: {direction}")

        super().move(movement)

    def die(self):
        self.is_alive = False

class King(BaseChessPiece):
    def __init__(self, color, identifier, position):
        super().__init__(color, 'King', 'K', identifier, position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self, direction: str, squares: int = 1):
        # King moves one square in any direction (squares should be 1)
        if squares != 1:
            raise ValueError("King can only move 1 square")

        d = direction.lower()
        if d in ('left', 'right', 'forward', 'backward'):
            if d == 'left':
                movement = BoardMovement.left(self.position, 1)
            elif d == 'right':
                movement = BoardMovement.right(self.position, 1)
            elif d == 'forward':
                movement = BoardMovement.forward(self.position, self.color, 1)
            else:
                movement = BoardMovement.backward(self.position, self.color, 1)
        else:
            # diagonal
            if d == 'forward-left':
                movement = BoardMovement.forward_left(self.position, self.color, 1)
            elif d == 'forward-right':
                movement = BoardMovement.forward_right(self.position, self.color, 1)
            elif d == 'backward-left':
                movement = BoardMovement.backward_left(self.position, self.color, 1)
            elif d == 'backward-right':
                movement = BoardMovement.backward_right(self.position, self.color, 1)
            else:
                raise ValueError(f"Unknown direction for King: {direction}")

        super().move(movement)

    def die(self):
        self.is_alive = False