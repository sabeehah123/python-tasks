board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    print ("\nBattleship field")
    for row in board:
        print ("".join(row))

print_board(board)

count=0

while count != 30:
    user_row=int(input("Enter row number: "))
    user_column=int((input("Enter column number: ")))

# patrol boat
    if user_row == 0 and user_column == 0:
        print("You hit a patrol boat")
        board[user_row][user_column] = "X"
        if board[0][0] == "X" and board[0][1] == "X":
            print("You sank a patrol boat")

    if user_row == 0 and user_column == 1:
        print("You hit a patrol boat")
        board[user_row][user_column] = "X"
        if board[0][0] == "X" and board[0][1] == "X":
            print("You sank a patrol boat")



# patrol baot 2

    if user_row == 0 and user_column == 3:
        print("You hit a patrol boat")
        board[user_row][user_column] = "X"
        if board[0][3] == "X" and board[0][4] == "X":
            print("You sank a patrol boat")

    if user_row == 0 and user_column == 4:
        print("You hit a patrol boat")
        board[user_row][user_column] = "X"
        if board[0][3] == "X" and board[0][4] == "X":
            print("You sank a patrol boat")

# battleship
    if user_row == 1 and user_column == 1:
        print("You hit a Battleship")
        board[user_row][user_column] = "X"
        if board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X" :
            print("You sank a Battleship")

    if user_row == 1 and user_column == 2:
        print("You hit a Battleship")
        board[user_row][user_column] = "X"
        if board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X":
            print("You sank a Battleship")

    if user_row == 1 and user_column == 3:
        print("You hit a Battleship")
        board[user_row][user_column] = "X"
        if board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X":
            print("You sank a Battleship")

#Battleship 2

    if user_row == 3 and user_column == 0:
        print("You hit a Battleship")
        board[user_row][user_column] = "X"
        if board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X":
            print("You sank a Battleship")

    if user_row == 3 and user_column == 1:
        print("You hit a Battleship")
        board[user_row][user_column] = "X"
        if board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X":
            print("You sank a Battleship")

    if user_row == 3 and user_column == 2:
        print("You hit a Battleship")
        board[user_row][user_column] = "X"
        if board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X":
            print("You sank a Battleship")

#submarine

    if user_row == 2 and user_column == 0:
        print("You hit a submarine")
        board[user_row][user_column] = "X"
        if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("You sank a submarine")

    if user_row == 2 and user_column == 1:
        print("You hit a submarine")
        board[user_row][user_column] = "X"
        if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("You sank a submarine")

    if user_row == 2 and user_column == 2:
        print("You hit a submarine")
        board[user_row][user_column] = "X"
        if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("You sank a submarine")

#destroyer

    if user_row == 4 and user_column == 2:
        print("You hit a Destroyer")
        board[user_row][user_column] = "X"
        if board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X":
            print("You sank a Destroyer")

    if user_row == 4 and user_column == 3:
        print("You hit a Destroyer")
        board[user_row][user_column] = "X"
        if board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X":
            print("You sank a Destroyer")

    if user_row == 4 and user_column == 4:
        print("You hit a Destroyer")
        board[user_row][user_column] = "X"
        if board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X":
            print("You sank a Destroyer")

    if user_row == 4 and user_column == 5:
        print("You hit a Destroyer")
        board[user_row][user_column] = "X"
        if board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X":
            print("You sank a Destroyer")

#Carrier
    if user_row == 5 and user_column == 1:
        print("You hit a Carrier")
        board[user_row][user_column] = "X"
        if board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][
            4] == "X":
            print("You sank a Carrier")

    if user_row == 5 and user_column == 2:
        print("You hit a Carrier")
        board[user_row][user_column] = "X"
        if board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][
            4] == "X":
            print("You sank a Carrier")

    if user_row == 5 and user_column == 3:
        print("You hit a Carrier")
        board[user_row][user_column] = "X"
        if board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][
            4] == "X":
            print("You sank a Carrier")

    if user_row == 5 and user_column == 4:
        print("You hit a Carrier")
        board[user_row][user_column] = "X"
        if board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][
            4] == "X":
            print("You sank a Carrier")

    if user_row == 5 and user_column == 0:
        print("You hit a Carrier")
        board[user_row][user_column] = "X"
        if board[5][0] == "X" and board[5][1] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][
            4] == "X":
            print("You sank a Carrier")


    if (user_row < 0 or user_row > 5) or (user_column < 0 or user_column > 5):
        print("Wrong coordinates")

    if (user_row == 0 and user_column == 2) or (user_row == 0 and user_column == 5) or (user_row == 1 and user_column == 0) or (user_row == 1 and user_column == 4) or (user_row == 1 and user_column == 5) or (user_row == 2 and user_column == 3) or (user_row == 2 and user_column == 4) or (user_row == 2 and user_column == 5) or (user_row == 3 and user_column == 3) or (user_row == 3 and user_column == 4) or (user_row == 3 and user_column == 5) or (user_row == 4 and user_column == 0) or (user_row == 4 and user_column == 1) or (user_row == 5 and user_column == 5):
        print("You missed! try again ")
        board[user_row][user_column] = "."

    print_board(board)
    if board[0][0] == "X" and board[0][1] == "X" and board[0][3] == "X" and board[0][4] == "X" and board[1][1] == "X" and board[1][2] == "X" and board[1][3] == "X" and board[3][0] == "X" and board[3][1] == "X" and board[3][2] == "X" and  board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" and board[4][2] == "X" and board[4][3] == "X" and board[4][4] == "X" and board[4][5] == "X" and board[5][0] == "X" and board[5][2] == "X" and board[5][3] == "X" and board[5][4] == "X" and board[5][
            1] == "X":
        print("Congratulations you sank all the ships and wasted my time to program this! You Won!!!!")
        break;


    count += 1

else:
    print ("Game over")


