import sys

# Represents a red or yellow piece which is inserted 
# into a column in the board.
class Token:
    def __init__(self):
        # (x_pos,y_pos) = (0,0) is the upper leftmost position on the board.
        self.x_pos = -1 # Column no. in board.
        self.y_pos = -1 # Row no. in board.
        self.colour = None # Should be either red or yellow.
    
    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def get_colour(self):
        return self.colour

    def set_x_pos(self, x_pos):
        self.x_pos = x_pos
    
    def set_y_pos(self, y_pos):
        self.y_pos = y_pos
    
    def set_colour(self, colour):
        self.colour = colour

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
    
    def get_grid(self):
        return self.grid

    # Scans selected column from the bottom and returns the row index
    # of the first occurring 0.
    def get_next_empty_row_no(self, column_no = None):
        if (column_no == None):
            raise ValueError('column_no cannot be \'None\'!')
        if (column_no >= self.get_width()):
            raise IndexError('column_no is out of bounds!')
        lst_col = self.grid.get_col(column_no)
        # Index from bottom of column to top 
        for i in range((len(lst_col)-1), -1, -1):
            if(lst_col[i] == 0):
                return i # return row_no
        return -1 # empty row not found

    # Drops given token down column specified.
    def drop_token(self, column_no = None, token = None):
        if (token == None):
            raise ValueError('token cannot be \'None\'!')
        row_no = self.get_next_empty_row_no(column_no)
        # token.set_x_pos(row_no)
        # token.set_y_pos(column_no)
        self.grid.set_item(row = row_no, col = column_no, val = token)

    def check_win(self):
        return false, -1
    
# Entry point.
if __name__ == "__main__":
    
    # Acquire cmd line args.
    args = sys.argv
    
    # Show error msg then exit if no data file name or too many args given.
    if len(args) < 2 or len(args) > 2:
        print('connectz.py: Provide one input file')
        sys.exit(-1)
    
    # Read game file.
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(str(9)) # File error.
        exit(9)
    
    # Extract dimensions (x,y,z) from first line of file.
    dimensions = f.readline().strip().split()
    
    # Illegal game cases:
    #   -Line length is greater than width
    #   -Line length is greater than height
    if(dimensions[2] > dimensions[0]):
        print(7) # Illegal game
        exit(7) 
    if(dimensions[2] > dimensions[1]):
        print(7) # Illegal game
        exit(7) 

    # Initialise a game board.
    board = Board(x = dimensions[0], y = dimensions[1], z = dimensions[2])
    
    # Track line number
    line_index = 0 

    # Track illegal continue attempts.
    won = False

    # Each subsequent row in file is a single move, alternating between players.
    for line in f:
        
        # If the game was already won after previous move, terminate.
        if won:
            print(4) # Illegal continue
            exit(4)

        move = line.strip()

        # Make a move:
        # ...odd line numbers are moves by player 1.
        if(line_index % 2 == 0):
            try:
                board.drop_token(column_no = , token = 1)
            except (ValueError, IndexError) as e:
                # Determine if illegal row or column.
                print(e)
        # ...even line numbers are moves by player 2.
        if(line_index % 2 == 1):
            try:
                board.drop_token(column_no = , token = 1)
            except (ValueError, IndexError) as e:
                # Determine if illegal row or column.
                print(e)

        # Check line length for winning combo.
        won, player_no = check_win()

        # Declare winner and terminate.
        if won:
            print(player_no) # Game won
        
        # Could be a number of reasons as to why there wasn't a winner:
        #   -Draw
        #   -
        elif not won:
            pass
        line_index += 1
        
    # Cleanup.
    f.close()
