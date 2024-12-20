'''
Connect 4
Day 1

Description: Created Board 2D array and a display for the board in the console.
'''

# Create board array
board = []
for col in range(7):                    # Repeat for each of the 7 columns
    board.append([])                    # Add an array per column
    for row in range(6):                # Repeat for each of the 6 rows
        board[col].append("-")          # Add a dash per row (So we can see what's happening for the time being)

# Display the game
def displayBoard():
    for row in range(5, -1, -1):            # Starting from row 5 on the board, display each row underneath (In other words, repeat where row = 5, then 4, then 3, then 2, then 1, then 0) 
        for col in range(7):                # Repeat for each column (col = 0, then 1, then 2, then 3, then 4, then 5, then 6)
            print(board[col][row], end=" ") # Display each point on the board, and do not go to the next line.
        print()                             # Go to the next line after doing all the values on a column
    print("1 2 3 4 5 6 7")                  # Display the columns underneath

displayBoard()                          # Output of what we did so far today, creating a board array and a display for it
