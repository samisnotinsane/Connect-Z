import sys

# Represents a connect-z board.
class Board:
    # x: width, y: height, z: min to win
    def __init__(self,):
        self.matrix = [] # board will be represented with a matrix
    
    # Creates a blank board using matrix representation
    # '0' represents a position in the board that is untouched.
    def init_board(self):
        self.matrix = [0] * self.x
        for row in range(self.y):
            self.matrix[row] = [0] * self.x

    # Open file from specified path and parse data into Board object.
    def load_file(self, path):
        # Read config file and parse data.
        f = open(path, "r")

        gameConfigRaw = f.readline()
        # Get rid of whitespace following readline
        gameConfig = gameConfigRaw.strip() 
        dimension = gameConfig.split() # 0,1,2 -> x,y,z
        self.x = int(dimension[0])
        self.y = int(dimension[1])
        self.z = int(dimension[2])
        moves = []
        for line in f:
            strippedLine = line.strip()
            moves.append(strippedLine)
        f.close()
        return moves

    def print_matrix(self):
        print('---BOARD_MATRIX---' + '\n')
        for row in range(len(self.matrix)):
            print(' | ' + str(self.matrix[row]) + ' | ' + '\n')
            # pass
        print('------------------')
        return '' # Avoid printing 'None' in stdio

    def print_list(self):
        print('---BOARD_LIST---')
        print(self.matrix)
        print('----------------')
        return '' # Avoid printing 'None' in stdio

    # Inserts a token down a specified column.
    #   Lack of token in board is marked by '0'
    #   Presence of token is marked by '1'.
    def insert(self, column, var):
        totalRowCount = len(self.matrix)
        currentRow = 0
        for row in range(totalRowCount):
            # Insert if last row and 0
            if row == totalRowCount-1:
                # We're now at the last row of selected column
                if self.matrix[row][column-1] == 0:
                    # Last row value was 0
                    self.matrix[row][column-1] = var
                elif self.matrix[row][column-1] == 1 or self.matrix[row][column-1] == 2:
                    # Last row value was 1
                    # Check for 0, bottom to top
                    for reverseRowPtr in range(totalRowCount-2, -1, -1):
                        if self.matrix[reverseRowPtr][column-1] == 0:
                            self.matrix[reverseRowPtr][column-1] = var
                            break
            currentRow += 1
                        
# -----------------------------------------------------

print('ConnectZ - 2018 Sameen Islam')
print('----------------------------')

argList = sys.argv
print('[DEBUG] args supplied: ' + str(len(argList)))
print('[DEBUG] args:' + str(argList))

# Show error msg then exit if no data file name or too many args given.
if len(argList) < 2 or len(argList) > 2:
    print('connectz.py: Provide one input file')
    sys.exit(-1)

print('[DEBUG] Loading, please wait...')
b = Board()
moves = b.load_file(argList[1])
b.init_board()
print('[DEBUG] Loading completed!')
print('[DEBUG] dimension (x,y,z): (' + str(b.x) + ',' + str(b.y) + ',' + str(b.z) + ')')
print('[DEBUG] total moves:' + str(moves))

# A game is illegal if z is greater than x, y or both
if b.z > b.x or b.z > b.y:
    print('[OUT] ' + str(7))

totalRowCount = len(b.matrix)
# print('[DEBUG] totalRowCount:' + str(totalRowCount))

# test_moves = [1,1,1]
# print('[DEBUG] test_moves:' + str(test_moves))
moveIndex = 0
# Play out the moves.
for move in range(len(moves)):
    remMoves = moves[moveIndex:len(moves)]
    print('[DEBUG] moves remaining: ' + str(remMoves))
    
    if (move % 2) == 0:
        # This is a move made by player one.
        print('[DEBUG] player \'A\' drops in column ' + str(moves[move]))
        b.insert(column=int(moves[move]), var=1)
    if (move % 2) == 1:
        # This move is by player two.
        print('[DEBUG] player \'B\' drops in column ' + str(moves[move]))        
        b.insert(column=int(moves[move]), var=2)
    
    print('[DEBUG] move #:' + str(moveIndex))
    print('[DEBUG] board state:')
    print(b.print_list())
    print(b.print_matrix())
    
    moveIndex += 1
    

# print('[DEBUG] board state:' + str(b.matrix))

print('----------------------------')
