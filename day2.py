# Create board array
board = []
for col in range(7):                    # Repeat for each column
    board.append([])                    # Add an array per column
    for row in range(6):                # Repeat for each row
        board[col].append("_")          # Add an underscore per row (So we can see what's happening for the time being)

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
    
    return True                             # Input is valid (integer from 1 to 7)

# Adds the input to the array
def playMove(input):
    pass                                # To be continued

# Main Loop
while True:
    # Display board and player's turn
    displayBoard()                          
    print(turn, "'s Turn!", sep="")

    # Prompt player input
    placement = input()

    #Checks if input is valid
    if isValidInput(placement):
        playMove(placement)             # Adds the input to the array
    else:
        print("Invalid Input")          # Outputs error is input is invalid