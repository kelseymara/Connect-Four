"""
Kelsey Marantan

Basic Implementation of Connect Four- Version 1
"""

"""
Connect Four Board is 6 rows x 7 columns
Use as Constant Variables to make code more flexible/easier to maintain
"""
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    # Create a 6x7 board filled with empty spaces
    board = []
    for index in range(ROW_COUNT):
        row = [' '] * COLUMN_COUNT
        board[index] = row
    return board

def print_board(board):
    # Print the current state of the board with only column labels
    col_nums = ' '.join(map(str, range(1, COLUMN_COUNT + 1)))  # Column numbers with space
    print(col_nums)  # Print column numbers
    print(' ' + '-' * (COLUMN_COUNT * 2 - 1))  # Separator line

    for row in board:
        print('|'.join(row))
        print('-' * (COLUMN_COUNT * 2 - 1))  # Separator line

def drop_piece(board, col, piece):
    # Place a game piece in the lowest available row in the specified column
    for row in range(ROW_COUNT - 1, -1, -1): # C++ version: for (int row = ROW_COUNT - 1; row >= 0; row--), row >=0 so it includes first row
        if board[row][col] == ' ':
            board[row][col] = piece
            return True  # Piece successfully dropped
    return False  # Column is full, cannot drop piece

def is_valid_location(board, col):
    # Check if a column is not full
    return board[0][col] == ' '

def winning_move(board, piece):
   # Check horizontally,  For each row, the inner loop iterates through the first 4 columns 
    
    for row in range(6): # Connect Four has 6 rows
        for col in range(4): # Only need to go through 4 columns 
            if all(board[row][col+i] == piece for i in range(4)):
                return True

    # Check vertically
    for row in range(3):
        for col in range(7):
            if all(board[row+i][col] == piece for i in range(4)):
                return True

    # Check diagonals
    for row in range(3):
        for col in range(4):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True
            if all(board[row+i][col+3-i] == piece for i in range(4)):
                return True

    return False

def main():
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)  # Print the initial board

    while not game_over:
        if turn % 2 == 0:
            piece = 'X'
        else:
            piece = 'O'

        col = int(input(f"Player {piece}, choose a column (1-{COLUMN_COUNT}): ")) - 1

        if is_valid_location(board, col):
            if drop_piece(board, col, piece):
                print_board(board)  # Print the board after dropping the piece

                if winning_move(board, piece):
                    print(f"Player {piece} wins!")
                    game_over = True

                turn += 1
            else:
                print("Column is full. Please choose a different column.") # if Column is full 
        else:
            print("Invalid column. Please choose a column within the range.") # if User does not pick a column within range

    print("Game Over")

if __name__ == "__main__":
    # Call the main function to start the Connect Four game.
    main()  