import random

# Step 1: Initialize Board
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# Step 2: Display Board
def display_board(board):
    for row in board:
        print(" | ".join(row))

# Step 3: Player Move
def player_move():
    while True:
        try:
            row = int(input("Enter the row number (0, 1, or 2): "))
            col = int(input("Enter the column number (0, 1, or 2): "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input")
                continue

            return row, col

        except ValueError:
            print("Invalid input")

# Step 4: Check Valid Move
def is_valid_move(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == "_"
    else:
        return False

# Step 5: Check Winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return row[0]
            
    # Check row
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col]
    
    # Check columns
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0]
        
    # Check diagonals    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return board[0][2]

    return None

# Step 6: Check Tie
def check_tie(board):
    return not any("_" in row for row in board) and not check_winner(board)

# Step 7: AI Move
def ai_move(board):
    empty_spots = [(row, col) for row in range(3) for col in range(3) if board[row][col] == "_"]
    return random.choice(empty_spots)

# Step 8: Game Loop
def play_game():
    global board
    
    while True:
        display_board(board)
        
        print("It's your turn (X)")
        x_row, x_col = player_move()
        
        while not is_valid_move(board, x_row, x_col):
            print("Invalid move. Please choose an empty space")
            x_row, x_col = player_move()
        
        board[x_row][x_col] = "X"
        
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a Tie")
            break
        
        display_board(board)
        print("It's the Computer's Turn (O)")
        o_row, o_col = ai_move(board)
        board[o_row][o_col] = "O"
        
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a Tie")
            break

# Step 9: Start the Game
play_game()
