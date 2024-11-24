'''
Connect 4
Final Code

Description: Slight code improvements using product() function from itertools, added a detection for if the
    game is a tie, colored the display using ANSI colors, other slight modifications to the display
'''

from itertools import product
# Create board array
board = []
for col in range(7):                    # Repeat for each column
    board.append([])                    # Add an array per column
    for row in range(6):                # Repeat for each row
        board[col].append(" ")          # Add an underscore per row (So we can see what's happening for the time being)

# Define a variable for whose turn it is
turn = "O" # Note: I'll use "O" and "X" as the players, as in tic-tac-toe

# Define number of empty spaces remaining on the board
spacesRemaining = 42

# Create a dictionary for what color to use for each space
# Colors found here: https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
spaceColors = {
    " ": "",
    "O": "\033[101m",
    "X": "\033[103m",
    "reset": "\033[0m"
}

# Display the game
def displayBoard():
    for row in range(5, -1, -1):            # Starting from row 5, display each row underneath (In other words, repeat where row = 5, then 4, then 3, then 2, then 1, then 0) 
        print("|", end="")                  # Add "|" at the start of each row
        for col in range(7):                # Repeat for each column (col = 0, then 1, then 2, then 3, then 4, then 5, then 6)
            # Display each point on the board, and do not go to the next line.
            # Also color each point to be the color they were defined to be colored
            print(spaceColors[board[col][row]] + " " + board[col][row] + " " + spaceColors["reset"], end="|")
        print()                             # Go to the next line after doing all the values on a column
    print("  1   2   3   4   5   6   7")    # Display the columns underneath

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
    # Define turn and spacesRemaining in the function
    global turn
    global spacesRemaining
    
    # Loop through each row of the input column to find the bottommost empty row
    for row, index in enumerate(board[input]):
        if index == " ":                    # Repeat until it sees " "
            board[input][row] = turn        # Change the value of the given point from being empty to be the player
            break                           # End the loop
    turn = "X" if turn == "O" else "O"      # If it was X's turn, then it will become O's turn now, and vice versa
    spacesRemaining -= 1                    # Decrease the number of empty spaces by 1

# Detects if someone wins
def detectWin():
    # Horizontal cases
    for col, row in product(range(4), range(6)):    # Repeat for the all pieces on the bottom 4 rows
        thisPiece = board[col][row]     # Sets the current piece
        if thisPiece == " ":            # Skip this point if it's empty
            continue
        for index in range(1, 4):       # Check if the next 3 pieces above are the same piece as the current one
            if board[col + index][row] != thisPiece:
                break                   # If the pieces are not the same, then go to the next point
            if index == 3:              # If all of the pieces are the same, then return who won the game
                return thisPiece

    # Vertical cases
    for col, row in product(range(7), range(3)):    # Repeat for the all pieces on the left 4 rows        
        thisPiece = board[col][row]     # Sets the current piece
        if thisPiece == " ":            # Skip this point if it's empty
            continue
        for index in range(1, 4):       # Check if the next 3 pieces to the right are the same piece as the current one
            if board[col][row + index] != thisPiece:
                break                   # If the pieces are not the same, then go to the next point
            if index == 3:              # If all of the pieces are the same, then return who won the game
                return thisPiece
    
    # Up and Right cases
    for col, row in product(range(4), range(3)):    # Repeat for the all pieces on the bottom left 12 points
        thisPiece = board[col][row]     # Sets the current piece
        if thisPiece == " ":            # Skip this point if it's empty
            continue
        for index in range(1, 4):       # Check if the next 3 pieces to the right are the same piece as the current one
            if board[col + index][row + index] != thisPiece:
                break                   # If the pieces are not the same, then go to the next point
            if index == 3:              # If all of the pieces are the same, then return who won the game
                return thisPiece

    # Down and Right cases
    for col, row in product(range(4), range(3, 6)): # Repeat for the all pieces on the top left 12 points
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
        displayBoard()
        print("O WINS!")
        break
    elif detectWin() == "X":
        displayBoard()
        print("X WINS!")
        break
    # If no spaces are left, prompt a draw
    if spacesRemaining == 0:
        displayBoard()
        print("IT'S A DRAW!")
        break