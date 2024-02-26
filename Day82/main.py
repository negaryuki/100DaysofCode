# Task: build a text-based version of the Tic Tac Toe game. The game should be playable in the command line. It should be a 2-player game, where one person is "X" and the other plays "O". build an AI player to play the game with the player.


#Step 1: Initialize Board

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# ALTERNATIVE : board = ["_" for _ in range(9)]

# Step 2: display Board and update it.

# the below function displays the current state of the Tic Tac Toe board in the command line interface.

# Parameters:
# board (list of lists or list): The current state of the Tic Tac Toe board.

def display_board(board):
  for row in board:
    print(" | ".join(row))    
    
display_board(board)

#Step 3: prompt input from the player to choose their move. 

def player_move():
  while True:
    try:
      row = input("Enter the row number (0,1 or 2)")
      column = input("Enter column row number (0,1 or 2)")
      
      # check input validation
      if row not in [0,1,2] or column not in [0,2,3]:
        print("Invalid input")
        continue
        
      return row,column
        
    except ValueError:
      print("invalid input")
      
# IMPORTANT: without the if statement, the function might continue with invalid input even after catching the exception.
# The if statement provides an additional layer of validation to ensure that the row and column values entered by the user are within the expected range 

#Step 4: write a function that validates the movement. wether there is an empty space or not


def is_valid_move(board,row,col):
  if 0 <= row < len(board) and 0 <= col < len(board):
    return board[row][col] == "_"
  else:
    return False
            
# Step 5: Checking if there is a winner or not

def check_winner(board):

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return board[0][2]

    # If no winner is found
    return None
