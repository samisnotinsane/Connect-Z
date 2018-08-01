import sys

# Represents a connect-z board.
class Board:
    # x: width, y: height, z: min to win
    def __init__(self,):
        self.x = -1
        self.y = -1
        self.z = -1
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
        m = []
        for line in f:
            strippedLine = line.strip()
            m.append(strippedLine)
        f.close()
        return m

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

    def verticalCheck(self, row, col):
        zInARow = False
        consecutiveCount = 0
        for i in range(row, self.y):
            if self.matrix[row][col] == self.matrix[i][col]:
                consecutiveCount += 1
            else:
                break
            if consecutiveCount >= self.z:
                zInARow = True
                if self.matrix[row][col] == 1:
                    print('p1 wins on vertical, col: ' + str(col+1))
                elif self.matrix[row][col] == 2:
                    print('p2 wins on vertical, col: ' + str(col+1))
                return zInARow

    def horizontalCheck(self, row, col):
        threeInARow = False
        consecutiveCount = 0
        # From starting position to end of row...
        for j in range(col, self.x):
            if self.matrix[row][col] == self.matrix[row][j]:
                consecutiveCount += 1
            else:
                break
            if consecutiveCount >= 3:
                threeInARow = True
                if self.matrix[row][col] == 1:
                    print('p1 wins on horizontal, row: ' + str(row+1))
                elif self.matrix[row][col] == 2:
                    print('p2 wins on horizontal, row: ' + str(row+1))
                return threeInARow
    
    def diagonalCheck(self, row, col):
        print('row: ' + str(row) + ', col: ' + str(col))
        threeInARow = False
        count = 0
        slope = None

        consecutiveCount = 0
        j = col
        print('scanning positive slope...')
        for i in range(row, self.x):
            print('i: ' + str(i) + ', j: ' + str(j))
            if j >= self.y:
                break
            elif self.matrix[row][col] == self.matrix[i][j]:
                consecutiveCount += 1
            else:
                break
            # Move along 1 col, 1 row to essentially move 1 down diagonally
            j += 1

        if consecutiveCount >= 3:
            count += 1 
            slope = 'positive'
            if self.matrix[row][col] == 1:
                print('p1 wins on diagonal, slope: ' + slope)
            elif self.matrix[row][col] == 2:
                print('p2 wins on diagonal, slope: ' + slope)
        
        consecutiveCount = 0
        j = col
        print('scanning negative slope...')
        for i in range(row, -1, -1):
            if j >= self.y:
                break
            elif self.matrix[row][col] == self.matrix[i][j]:
                consecutiveCount += 1
            else:
                break
            # Move along 1 col, -1 row to essentially move 1 up diagonally
            j += 1

        if consecutiveCount >= 3:
            count += 1
            slope = 'negative'
            if self.matrix[row][col] == 1:
                print('p1 wins on diagonal!')
            elif self.matrix[row][col] == 2:
                print('p2 wins on diagonal!')
        
        if count > 0:
            print('count (>): ' + str(count))
            threeInARow = True
        if count == 2:
            print('count (==): ' + str(count))
            slope = 'both'
        return threeInARow, slope

    def checkForZ(self):
        # For each counter in the board...
        for i in range(self.y): # col elems
            for j in range(self.x): # row elems
                # We only check for z-in-a-row starting at (i,j)
                if self.matrix[i][j] != 0:
                    if verticalCheck(i, j):
                        finished = True
                        print('vertical match!')
                        break
                    if horizontalCheck(i, j):
                        finished = True
                        print('horizontal match!')
                        break
                    diag_threes, slope = diagonalCheck(i, j)
                    if diag_threes:
                        print('checkForZ/slope: ' + slope)
                        finished = True
                        break
    
    def play_moves(self, moves):
        moveIndex = 0
        # Play out the moves.
        for move in range(len(moves)):
            print('[DEBUG] move #: ' + str(moveIndex))
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
            print('[DEBUG] board state:')
            # print(b.print_list())
            print(b.print_matrix())
            moveIndex += 1

# -----------------------------------------------------

print('Connect Z - 2018')
print('Author: Sameen Islam')
print('----------------------------')

argList = sys.argv
print('[DEBUG] checking game: ' + str(argList[1]))
# Show error msg then exit if no data file name or too many args given.
if len(argList) < 2 or len(argList) > 2:
    print('connectz.py: Provide one input file')
    sys.exit(-1)

print('[DEBUG] loading, please wait...')
b = Board()
moves = b.load_file(argList[1])
b.init_board()
print('[DEBUG] loading complete!')

print('[DEBUG] dimension (x,y,z): (' + str(b.x) + ',' + str(b.y) + ',' + str(b.z) + ')')

# A game is illegal if z is greater than x, y or both
if b.z > b.x or b.z > b.y:
    print('[OUT] ' + str(7))

b.play_moves(moves)
b.checkForZ()

# print('[DEBUG] board state:' + str(b.matrix))

print('----------------------------')
