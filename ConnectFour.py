import numpy as np

# array representation
EMPTY = 0
RED = 1
BLUE = 2

# # string representation
# EMPTY_STR = '.'
# RED_STR = 'r'
# BLUE_STR = 'b'

COLORS = [EMPTY, RED, BLUE]

class ConnectFour:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.zeros(board_size, dtype='int32')
    
    def drop_piece(self, color, column):
        # indexing of column passed as args starts at zero
        # drops a piece of given color at the given column
        # returns true if move is successful, false otherwise 
        
        # checking and sanitizing input
        if column >= self.board_size[1] or column < 0:
            print('Invalid position')
            return False
        if color not in COLORS[1:]:
            print('Invalid color')
            return False

        # dropping piece
        column_to_drop = np.nonzero(self.board[:, column])
        row_to_change = np.amin(column_to_drop, initial = self.board_size[0]) - 1

        if row_to_change < 0: # column is full
            print('Invalid move: column is full')
            return False
        
        self.board[row_to_change, column] = color
        return True
    
    def is_game_over(self):
        if np.all(self.board > 0):  # board full
            return True
        return False

    def print_board(self):
        print(self.board)