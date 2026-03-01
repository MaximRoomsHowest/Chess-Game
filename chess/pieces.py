from abc import abstractmethod, ABC

class BaseChessPiece(ABC):
    def __init__(self, color, name, symbol, identifier, position):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = position
        self.is_alive = True

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def die(self):
        pass

class Pawn(BaseChessPiece):
    def __init__(self, color, position):
        super().__init__(color, 'Pawn', '-', 'pawn', position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        print("Pawn moves forward 1 position")

    def die(self):
        self.is_alive = False

class Rook(BaseChessPiece):
    def __init__(self, color, position):
        super().__init__(color, 'Rook', 'R', 'rook', position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        print("Rook moves in a straight line")

    def die(self):
        self.is_alive = False

class Bishop(BaseChessPiece):
    def __init__(self, color, position):
        super().__init__(color, 'Bishop', 'B', 'bishop', position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        print("Bishop moves diagonally")

    def die(self):
        self.is_alive = False

class Knight(BaseChessPiece):
    def __init__(self, color, position):
        super().__init__(color, 'Knight', 'N', 'knight', position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        print("Knight moves in an L shape")

    def die(self):
        self.is_alive = False

class Queen(BaseChessPiece):
    def __init__(self, color, position):
        super().__init__(color, 'Queen', 'Q', 'queen', position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        print("Queen moves in any direction")

    def die(self):
        self.is_alive = False

class King(BaseChessPiece):
    def __init__(self, color, position):
        super().__init__(color, 'King', 'K', 'king', position)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    
    def move(self):
        print("King moves one square in any direction")

    def die(self):
        self.is_alive = False