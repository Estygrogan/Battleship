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
    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >=self.num_ships:
            print("Error! You cannot print any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board [x] [y] = "@"

def check_coordinates():
    pass

def play_game():
    pass

def new_game():
    pass