from random import randint

scores = {"player": 0, "computer": 0}


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


def fill_board(board):
    """
    Function designed to populate our board with ships
    """
    x = random_point(board.size)
    y = random_point(board.size)
    board.add_ship(x, y)


def check_coordinates(board):
    """
    Function that will make sure coordinates are integers
    """
    try:
        x, y = int(x), int(y)
        board.board[x][y] in board.board

    except IndexError:
        print("You must enter a valid number to make a guess")
        return False

    if guess in guesses.board:
        print("You have already guessed these coordinates, guess again")
        return False


'''
def print_board(board):
    player_board.print()
    computer_board.print()
'''

def play_game(computer_board, player_board):
    """
    Defines rules while playing the game
    """
    while self.guesses > 0:
        if input("Please enter your guess") in ships.board:
            print("Successful hit, well done!")
            return True
        else:
            print("Miss! Try again")
            return False


def new_game():
    """
    Function that will run when the game starts
    """
    size = 5
    num_ships = 4
    scores["player"] = 0
    scores["computer"] = 0
    print("Welcome to Battleship! Press Enter to begin!")
    print(f" Board Size{size}, Number of Ships{num_ships}")
    print("Top left corner is row:0, col 0")
    print("-" * 35)
    player_name = input("Please enter your name \n")
    print("-" * 35)
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        fill_board(player_board)
        fill_board(computer_board)

    play_game(computer_board, player_board)


new_game()
