# 11.Recap1
import random

def diceGuess(guess):
  """
  This function generates a random number between 1 and 6 (inclusive) and checks if the user's guess is correct.

  Args:
      guess: The user's guess as an integer.

  Returns:
      True if the guess is correct, False otherwise.
  """
  # Generate a random number between 1 and 6
  random_number = random.randint(1, 6)

  # Check if the guess is correct
  return guess == random_number

# Example usage
if diceGuess(5):
  print("Correct!")
else:
  print("Incorrect.")



# 11.1a (initialise_board)
def initialise_board():
    # Create a 3x3 nested list using nested for loops
    board = []

    # Outer loop iterates 3 times (rows)
    for i in range(3):
        row = []
        # Inner loop iterates 3 times (columns)
        for i in range(3):
            row.append(' ')
        board.append(row)

    return board



# 11.2a (print_board)
def print_board(board):
    """Prints the Tic Tac Toe board with cells labelled from 1 to 9."""
    print("\nBoard Layout:")
    cell_number = 1
    for row in board:
        for cell in row:
            if cell != ' ':
                print(" " + str(cell) + " ", end="")
            else:
                print(" " + str(cell_number) + " ", end="")
            if cell_number % 3 != 0:
                print("|", end="")
            cell_number += 1
        if cell_number <= 9:
            print("\n----------")
    print("\n")



# 12.3a (get_player_move)
def get_player_move(board):
    move_input = input("Enter your move (1-9): ")
    move = int(move_input) - 1
    row = move // 3
    col = move % 3
    board[row][col] = 'X'

# Main game loop
board = initialise_board()
print_board(board)
get_player_move(board)
    


# 12.3b (get_player_move)
# Main game loop
board = initialise_board()
while True:
    print_board(board)
    get_player_move(board)



# 12.3c (get_player_move)
def get_player_move(board):
    move_input = input("Enter your move (1-9): ")
    if move_input.isdigit():
        move = int(move_input) - 1
        row = move // 3
        col = move % 3
        board[row][col] = 'X'
    else:
        print("Invalid input. Please enter a number.")



# 12.3d (get_player_move)
def get_player_move(board):
    move_input = input("Enter your move (1-9): ")
    if move_input.isdigit():
        if int(move_input) >= 1 and int(move_input) <= 9:
            move = int(move_input) - 1
            row = move // 3
            col = move % 3
            board[row][col] = 'X'
        else:
            print("Please enter a number between 1 and 9.")
    else:
        print("Invalid input. Please enter a number.")



# 12.3e (get_player_move)
def get_player_move(board):
    move_input = input("Enter your move (1-9): ")
    if move_input.isdigit():
        if int(move_input) >= 1 and int(move_input) <= 9:
            move = int(move_input) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("That spot is already taken or invalid. Please choose another.")
        else:
            print("Please enter a number between 1 and 9.")
    else:
        print("Invalid input. Please enter a number.")

# 12.4a (check_win)
win_conditions = [
    # Horizontal
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    # Vertical
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    # Diagonal
    [board[0][0], board[1][1], board[2][2]],
    [board[2][0], board[1][1], board[0][2]],
]



# 12.4b (check_win)
def check_win(board):
    """Checks if there is a win condition on the board."""
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    for condition in win_conditions:
        if condition[0] == condition[1] == condition[2] and condition[0] != ' ':
            return True
    return False



# 13.3f (get_player_move)
def get_player_move(current_player, board):
    move_input = input("Player " + current_player + ", enter your move (1-9): ")
    if move_input.isdigit():
        if int(move_input) >= 1 and int(move_input) <= 9:
            move = int(move_input) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("That spot is already taken or invalid. Please choose another.")
        else:
            print("Please enter a number between 1 and 9.")
    else:
        print("Invalid input. Please enter a number.")



# 13.5a (switch_player)
def switch_player(current_player):
    """Switches the current player."""
    if current_player == "X":
        return "0"
    else:
        return "X"



# 13.mainGameLoop
board = initialise_board()
current_player = 'X'
while True:
    print_board(board)
    get_player_move(current_player, board)
    if check_win(board):
        print_board(board)
        print("Player " + current_player + " wins!")
        break
    current_player = switch_player(current_player)



# 13.6a (check_full)
def check_full(board):
    """Checks if the board is full and there is a draw."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True



# Main Game Loop
board = initialise_board()
current_player = 'X'
while True:
    print_board(board)
    get_player_move(current_player, board)
    if check_full(board) and not check_win(board):
        print_board(board)
        print("It's a draw!")
        break
    elif check_win(board):
        print_board(board)
        print("Player " + current_player + " wins!")
        break
    current_player = switch_player(current_player)



# Main Game Loop (Improved)
board = initialise_board()
current_player = 'X'
while True:
    print_board(board)
    get_player_move(current_player, board)
    if check_win(board):
        print_board(board)
        print("Player " + current_player + " wins!")
        break
    elif check_full(board):
        print_board(board)
        print("It's a draw!")
        break
    current_player = switch_player(current_player)