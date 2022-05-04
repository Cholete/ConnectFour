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
        self.rows = board_size[0]
        self.cols = board_size[1]
        self.board = np.zeros(board_size, dtype='int32')
    
    def drop_piece(self, color, column):
        # indexing of column passed as args starts at zero
        # drops a piece of given color at the given column
        # returns true if move is successful, false otherwise 
        
        # checking and sanitizing input
        if column >= self.cols or column < 0:
            print('Invalid position')
            return False
        if color not in COLORS[1:]:
            print('Invalid color')
            return False

        # dropping piece
        column_to_drop = np.nonzero(self.board[:, column])
        row_to_change = np.amin(column_to_drop, initial = self.rows) - 1

        if row_to_change < 0: # column is full
            print('Invalid move: column is full')
            return False
        
        self.board[row_to_change, column] = color
        return True
    
    def is_game_over(self):
        if np.all(self.board > 0):  # board full
            return True
        if self.has_connect_four():
            return True
        return False

    def has_connect_four(self):
        # directions
        move_right = (0, 1)
        move_down = (-1, 0)
        move_diag_positive = (-1, 1)
        move_diag_negative = (-1, -1)

        # rows - move from start of a row to end
        for i in range(self.rows):
            if self.__line_has_connect_four((i, 0), move_right):
                return True

        # columns - move from top of col to bottom
        for i in range(self.cols):
            if self.__line_has_connect_four((0, i), move_down):
                return True

        # positive slope - start at L formed by connecting top left, bottom left and bottom right
        for i in range(self.rows): # top left to bottom left
            if self.__line_has_connect_four((i, 0), move_diag_positive):
                return True
        for i in range(self.cols): # bottom left to bottom right
            if self.__line_has_connect_four((self.rows - 1, i), move_diag_positive):
                return True

        # negative slope - start at mirroed L formed by connecting top right, bottom right and bottom left
        for i in range(self.rows): # top right to bottom right
            if self.__line_has_connect_four((i, self.cols - 1), move_diag_negative):
                return True
        for i in range(self.cols - 1, -1, -1): # bottom right to bottom left
            if self.__line_has_connect_four((self.rows - 1, i), move_diag_negative):
                return True
        
        return False


    def __line_has_connect_four(self, start, direction):
        # start is a tuple representing the coords of start position
        # direction is a tuple representing change of position
        conn_color = EMPTY
        conn_count = 0
        current_coords = start
        while (self.is_valid_position(current_coords)):
            current = self.board[current_coords]
            if (current != EMPTY and current == conn_color):  # colors match
                    conn_count += 1
                    if conn_count >= 4: # connect 4 made
                        return True
            else: # colors don't match
                conn_color = current
                conn_count = 1
            current_coords = (current_coords[0] + direction[0], current_coords[1] + direction[1])

        return False

    def is_valid_position(self, position):
        # position is a tuple of coordinates
        return position[0] >= 0 and position[1] >= 0 and position[0] < self.rows and position[1] < self.cols  
        
    def print_board(self):
        print(self.board)