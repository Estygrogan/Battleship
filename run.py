class Board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        # Function that will print our board
        for row in self.board:
            print(" ".join(row))
    

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"
    
    if(x,y) in self.ships:
        self.board [x][y]="*"
        return hit
    else:
        return miss
