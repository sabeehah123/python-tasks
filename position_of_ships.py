board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    print ("Battleship field")
    for row in board:
        print ("".join(row))



# patrol boat 1
guess_row1 = 0
guess_col1 = 0
guess_row2 = 0
guess_col2 = 1
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"

# patrol boat 2

guess_row1 = 0
guess_col1 = 3
guess_row2 = 0
guess_col2 = 4
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"

# Battleship 1
guess_row1 = 1
guess_col1 = 1
guess_row2 = 1
guess_col2 = 2
guess_row3 = 1
guess_col3 = 3
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"
board[guess_row3][guess_col3] = "X"

# Battleship 2
guess_row1 = 2
guess_col1 = 0
guess_row2 = 2
guess_col2 = 1
guess_row3 = 2
guess_col3 = 2
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"
board[guess_row3][guess_col3] = "X"

# Submarine
guess_row1 = 3
guess_col1 = 0
guess_row2 = 3
guess_col2 = 1
guess_row3 = 3
guess_col3 = 2
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"
board[guess_row3][guess_col3] = "X"

# Destroyer
guess_row1 = 4
guess_col1 = 2
guess_row2 = 4
guess_col2 = 3
guess_row3 = 4
guess_col3 = 4
guess_row4 = 4
guess_col4 = 5
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"
board[guess_row3][guess_col3] = "X"
board[guess_row4][guess_col4] = "X"

# carrier


guess_row1 = 5
guess_col1 = 0
guess_row2 = 5
guess_col2 = 1
guess_row3 = 5
guess_col3 = 2
guess_row4 = 5
guess_col4 = 3
guess_row5 = 5
guess_col5 = 4
board[guess_row1][guess_col1] = "X"
board[guess_row2][guess_col2] = "X"
board[guess_row3][guess_col3] = "X"
board[guess_row4][guess_col4] = "X"
board[guess_row5][guess_col5] = "X"

print_board(board)