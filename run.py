from random import randint


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
        # Method that will print our board
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error! You cannot print any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def check_coordinates():
    pass


def fill_board(board):
    """
    Function designed to populate our board with ships
    """
    x = random_point(board.size)
    y = random_point(board.size)
    board.add_ship(x, y)


def play_game():
    pass


def player_name():
    input("Enter your name")


def new_game():
    size = 6
    num_ships = 4
    name = player_name
    type = "player"
    print("Welcome to Battleship! Press Enter to begin!")


new_game()
