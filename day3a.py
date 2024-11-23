# Create board array
board = []
for col in range(7):                    # Repeat for each column
    board.append([])                    # Add an array per column
    for row in range(6):                # Repeat for each row
        board[col].append(" ")          # Add an underscore per row (So we can see what's happening for the time being)

# Define a variable for whose turn it is
turn = "O" # Note: I'll use "O" and "X" as the players, as in tic-tac-toe

# Display the game
def displayBoard():
    for row in range(5, -1, -1):            # Starting from row 5, display each row underneath (In other words, repeat where row = 5, then 4, then 3, then 2, then 1, then 0) 
        for col in range(7):                # Repeat for each column (col = 0, then 1, then 2, then 3, then 4, then 5, then 6)
            print(board[col][row], end="")  # Display each point on the board, and do not go to the next line.
        print()                             # Go to the next line after doing all the values on a column
    print("1234567")                        # Display the columns underneath

# Checks if the player input is a valid input
def isValidInput(input):
    if not input.isdigit():                 # Returns false if the input is not an integer
        return False
    if int(input) < 1 or int(input) > 7:    # Returns false if the input is less than 1 or greater than 7
        return False                        # Note: input is a string, so we need to convert input into an integer using the "int()" function
    if board[int(input) - 1][5] != " ":     # Returns false if the inputted row is already full
        return False

    return True                             # Input is valid (integer from 1 to 7)

# Adds the input to the array
def playMove(input):
    # Define turn within the function
    global turn                             

    # Loop through each row of the input column to find the bottommost empty row
    for row, index in enumerate(board[input]):
        if index == " ":                    # Repeat until it sees " "
            board[input][row] = turn        # Change the value of the given point from being empty to be the player
            break                           # End the loop
    turn = "X" if turn == "O" else "O"      # If it was X's turn, then it will become O's turn now, and vice versa

# Detects if someone wins
def detectWin():
    # Horizontal cases
    for col in range(4):
        for row in range(6):                # Repeat for the all pieces on the bottom 4 rows
            thisPiece = board[col][row]     # Sets the current piece
            if thisPiece == " ":            # Skip this point if it's empty
                continue
            for index in range(1, 4):       # Check if the next 3 pieces above are the same piece as the current one
                if board[col + index][row] != thisPiece:
                    break                   # If the pieces are not the same, then go to the next point
                if index == 3:              # If all of the pieces are the same, then return who won the game
                    return thisPiece

    # Vertical cases
    for col in range(7):
        for row in range(3):                # Repeat for the all pieces on the left 4 rows
            thisPiece = board[col][row]     # Sets the current piece
            if thisPiece == " ":            # Skip this point if it's empty
                continue
            for index in range(1, 4):       # Check if the next 3 pieces to the right are the same piece as the current one
                if board[col][row + index] != thisPiece:
                    break                   # If the pieces are not the same, then go to the next point
                if index == 3:              # If all of the pieces are the same, then return who won the game
                    return thisPiece
    
    # Up and Right cases
    for col in range(4):
        for row in range(3):                # Repeat for the all pieces on the bottom left 12 points
            thisPiece = board[col][row]     # Sets the current piece
            if thisPiece == " ":            # Skip this point if it's empty
                continue
            for index in range(1, 4):       # Check if the next 3 pieces to the right are the same piece as the current one
                if board[col + index][row + index] != thisPiece:
                    break                   # If the pieces are not the same, then go to the next point
                if index == 3:              # If all of the pieces are the same, then return who won the game
                    return thisPiece

    # Down and Right cases
    for col in range(4):
        for row in range(3, 6):             # Repeat for the all pieces on the top left 12 points
            thisPiece = board[col][row]     # Sets the current piece
            if thisPiece == " ":            # Skip this point if it's empty
                continue
            for index in range(1, 4):       # Check if the next 3 pieces to the right are the same piece as the current one
                if board[col + index][row - index] != thisPiece:
                    break                   # If the pieces are not the same, then go to the next point
                if index == 3:              # If all of the pieces are the same, then return who won the game
                    return thisPiece

# Main Loop
while True:
    # Display board and player's turn
    displayBoard()                          
    print(turn, "'s Turn!", sep="")

    # Prompt player input
    placement = input()

    #Checks if input is valid
    if isValidInput(placement):
        playMove(int(placement) - 1)    # Adds the input to the array
    else:                               # Note: the input was from 1 to 7, but the array indexes from 0 to 6, so to fix this, we subtract the input by 1
        print("Invalid Input")          # Outputs error is input is invalid

    # Check if someone wins
    if detectWin() == "O":
        print("O WINS!")
        break
    elif detectWin() == "X":
        print("X WINS!")
        break