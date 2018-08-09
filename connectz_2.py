# Represents a red or yellow piece which is inserted 
# into a column in the board.
class Token:
    def __init__(self, colour):
        # (x_pos,y_pos) = (0,0) is the lower leftmost position on the board.
        self.x_pos = -1 # Column no. in board.
        self.y_pos = -1 # Row no. in board.
        self.colour = colour # Should be either red or yellow.

# A grid is a collection of scalar values arranged in rows and columns 
# as a matrix. The elements of the grid can be accessed by specifying 
# a given row and column index with indices starting at 0.
class Grid:
    # Initialise an [n_rows x n_cols] grid with 0's.
    def __init__(self, n_rows, n_cols):
        self.rows = [0] * n_rows
        for i in range(n_rows):
            self.rows[i] = [0] * n_cols

    # Returns the element held in specified row, column.
    def get_item(self, row = None, col = None):
        if (row == None):
            raise ValueError('row cannot be \'None\'!')
        if (col == None):
            raise ValueError('col cannot be \'None\'!')
        # Check specified row and column is within bounds.
        if (row <= self.num_rows()):
            if (col <= self.num_cols()):
                return self.rows[row][col]
            else:
                raise IndexError('col is out of bounds!')
        else:
            raise IndexError('row is out of bounds!')
    
    # Sets the given value as an element in specified row, column.
    def set_item(self, row = None, col = None, val = None):
        if (row == None):
            raise ValueError('row cannot be \'None\'!')
        if (col == None):
            raise ValueError('col cannot be \'None\'!')
        if (val == None):
            raise ValueError('val cannot be \'None\'!')
        # Check specified row and column is within bounds.
        if (row <= self.num_rows()):
            if (col <= self.num_cols()):
                self.rows[row][col] = val

    # Returns the number of rows in the grid.
    def num_rows(self):
        return len(self.rows)

    # Returns the number of columns in the grid.
    def num_cols(self):
        return len(self.rows[0])
    
    # Returns the elements of specified column as a list.
    def get_col(self, column_no):
        lst_col = []
        for i in range(self.num_rows()):
            lst_col.append(self.rows[i][column_no])
        return lst_col

# Represents a game board containing a grid which may hold a token as 
# an element.
# x represents the width of the board in columns.
# y represents the height of the board in rows.
# z represents the minimum no. of tokens in a straight line required to win the game.
class Board:
    def __init__(self, x, y, z):
        self.grid = Grid(n_cols = x, n_rows = y)
        self.line_length = z

    def get_width(self):
        return self.grid.num_cols()

    def get_height(self):
        return self.grid.num_rows()

    def get_line_length(self):
        return self.line_length

    def get_next_empty_pos(self, column_no = None):
        if (column_no == None):
            raise ValueError('column_no cannot be \'None\'!')
        if (column_no >= self.get_width()):
            raise IndexError('column_no is out of bounds!')
        return -1, -1

    def drop_token(self, column_no = None, token = None):
        row, col = get_next_empty_pos(column_no = 0)
        if (token == None):
            raise ValueError('token cannot be \'None\'!')
        
    def check_winner(self, colour):
        pass
    
