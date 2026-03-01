class BoardMovement:
    @staticmethod
    def forward(position: str, color: str = 'BLACK', squares: int = 1):
        """
        Move the piece forward on the board.
        """
        # Get the column and row of the current position
        column = position[0] # First character defines the columnn
        row = int(position[1]) # The second character is a numerical representation and defines the row.
        # Validate squares
        if squares < 1:
            raise ValueError("squares must be >= 1")

        # For WHITE pieces the board is flipped: forward moves toward decreasing row numbers
        if color.upper() == 'WHITE':
            new_row = row - squares
        else:
            # default: BLACK moves forward to increasing row numbers
            new_row = row + squares

        # Block when reaching beyond the board (rows must be 1..8)
        if new_row == 0 or new_row == 9 or new_row < 1 or new_row > 8:
            return None

        # Return the new position
        return f"{column}{new_row}"
    
    @staticmethod
    def backward(position: str, color: str = 'BLACK', squares: int = 1):
        """
        Move the piece backward on the board.
        """
        # Get the column and row of the current position
        column = position[0] # First character defines the columnn
        row = int(position[1]) # The second character is a numerical representation and defines the row.
        # Validate squares
        if squares < 1:
            raise ValueError("squares must be >= 1")

        # For WHITE pieces the board is flipped: backward moves toward increasing row numbers
        if color.upper() == 'WHITE':
            new_row = row + squares
        else:
            # default: BLACK moves backward to decreasing row numbers
            new_row = row - squares

        # Block when reaching beyond the board (rows must be 1..8)
        if new_row == 0 or new_row == 9 or new_row < 1 or new_row > 8:
            return None

        # Return the new position
        return f"{column}{new_row}"
    
    @staticmethod
    def left(position: str, squares: int = 1):
        """
        Move the piece left on the board.
        """
        # Get the column and row of the current position
        column = position[0] # First character defines the columnn
        row = int(position[1]) # The second character is a numerical representation and defines the row.
        # Validate squares
        if squares < 1:
            raise ValueError("squares must be >= 1")

        new_ord = ord(column) - squares
        new_column = chr(new_ord) if new_ord >= 0 else None

        # When reaching the edges the movement should be blocked. Columns must be 'a'..'h'
        # Note: subtracting 1 from 'a' results in '`' which should be blocked as described.
        if new_column is None or new_column == '`' or new_column == 'i' or new_ord < ord('a') or new_ord > ord('h'):
            return None

        # Return the new position
        return f"{new_column}{row}"
    
    @staticmethod
    def right(position: str, squares: int = 1):
        """
        Move the piece right on the board.
        """
        # Get the column and row of the current position
        column = position[0] # First character defines the columnn
        row = int(position[1]) # The second character is a numerical representation and defines the row.
        # Validate squares
        if squares < 1:
            raise ValueError("squares must be >= 1")

        new_ord = ord(column) + squares
        new_column = chr(new_ord) if new_ord <= 0x10FFFF else None

        # When reaching the edges the movement should be blocked. Columns must be 'a'..'h'
        # Note: adding 1 to 'h' results in 'i' which should be blocked as described.
        if new_column is None or new_column == '`' or new_column == 'i' or new_ord < ord('a') or new_ord > ord('h'):
            return None

        # Return the new position
        return f"{new_column}{row}"