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
        try:
            f = open(path, "r")
        except FileNotFoundError:
            print(str(9))
            exit(9)
        gameConfigRaw = f.readline()
        # Get rid of whitespace following readline
        gameConfig = gameConfigRaw.strip() 
        dimension = gameConfig.split() # 0,1,2 -> x,y,z
        try:
            self.x = int(dimension[0])
            self.y = int(dimension[1])
            self.z = int(dimension[2])
        except ValueError:
            print(str(8))
            exit(8)
        m = []
        for line in f:
            strippedLine = line.strip()
            m.append(strippedLine)
        f.close()
        return m

    # Debug method for visualising board as a matrix.
    def print_matrix(self):
        print('---BOARD_MATRIX---' + '\n')
        for row in range(len(self.matrix)):
            print(' | ' + str(self.matrix[row]) + ' | ' + '\n')
            # pass
        print('------------------')
        return '' # Avoid printing 'None' in stdio

    # Debug method for visualising board as a list.
    def print_list(self):
        print('---BOARD_LIST---')
        print(self.matrix)
        print('----------------')
        return '' # Avoid printing 'None' in stdio

    # Inserts a token down a specified column.
    #   Lack of token in board is marked by '0'
    #   Presence of token is marked by '1' or '2' depending on player.
    def insert(self, column, var):
        totalRowCount = len(self.matrix)
        currentRow = 0
        if column > len(self.matrix[0]):
            print(str(6)) # Illegal column
            exit(6)
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
                    placeFound = False
                    # Decrement from next row up (2nd last row).
                    for reverseRowPtr in range(totalRowCount-2, -1, -1):
                        if self.matrix[reverseRowPtr][column-1] == 0:
                            self.matrix[reverseRowPtr][column-1] = var
                            placeFound = True
                            break
                    if not placeFound:
                        print(str(5)) # Illegal row
                        exit(5)
            currentRow += 1

    def play_moves(self, moves):
        moveIndex = 0
        # Play out the moves.
        for move in range(len(moves)):
            remMoves = moves[moveIndex:len(moves)]
            if (move % 2) == 0:
                # This is a move made by player one.
                b.insert(column=int(moves[move]), var=1)
            if (move % 2) == 1:
                # This move is by player two.
                b.insert(column=int(moves[move]), var=2)
            moveIndex += 1

    def horizontalCheck(self, row, col):
        zInARow = False
        consecutiveCount = 0
        player = 0
        # From starting position to end of row...
        for j in range(col, 3):
            if self.matrix[row][col] == self.matrix[row][j]:
                consecutiveCount += 1
            else:
                break
            if consecutiveCount >= 3:
                zInARow = True
                if self.matrix[row][col] == 1:
                    player = 1
                elif self.matrix[row][col] == 2:
                    player = 2
        return zInARow, player

    def verticalCheck(self, row, col):
        zInARow = False
        consecutiveCount = 0
        player = 0
        for i in range(row, self.y):
            if self.matrix[row][col] == self.matrix[i][col]:
                consecutiveCount += 1
            else:
                break
            if consecutiveCount >= self.z:
                zInARow = True
                if self.matrix[row][col] == 1:
                    player = 1
                elif self.matrix[row][col] == 2:
                    player = 2
        return zInARow, player

    def diagonalCheck(self, row, col):
        zInARow = False
        count = 0
        player = 0
        consecutiveCount = 0
        j = col
        for i in range(row, self.x):
            if j >= self.y:
                break
            elif self.matrix[row][col] == self.matrix[i][j]:
                consecutiveCount += 1
            else:
                break
            # Move along 1 col, 1 row to essentially move 1 down diagonally
            j += 1
        if consecutiveCount >= self.z:
            count += 1 
            if self.matrix[row][col] == 1:
                player = 1
            elif self.matrix[row][col] == 2:
                player = 2
        consecutiveCount = 0
        j = col
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
            if self.matrix[row][col] == 1:
                player = 1
            elif self.matrix[row][col] == 2:
                player = 2
        if count > 0:
            zInARow = True
        return zInARow, player

    # Check if there's a z-in-a-row in the board
    def checkForZ(self):
        win = False
        winPlayer = 0
        winCount = 0
        # For each counter in the board...
        for i in range(self.y): # col elems
            for j in range(self.x): # row elems
                # We only check for z-in-a-row starting at (i,j)
                if self.matrix[i][j] != 0:
                    vertWin, player = self.verticalCheck(i, j)
                    if vertWin:
                        win = True
                        winPlayer = player
                        winCount += 1
                        break
                    horizWin, player = self.horizontalCheck(i, j)
                    if horizWin:
                        win = True
                        winPlayer = player
                        winCount += 1
                        break
                    diagWin, player = self.diagonalCheck(i, j)
                    if diagWin:
                        win = True
                        winPlayer = player
                        winCount += 1
                        break
        if winCount > 1:
            # Draw
            winPlayer = 0
            win = False
        return win, winPlayer

# ----------------------------BEGIN---------------------------------
argList = sys.argv

# Show error msg then exit if no data file name or too many args given.
if len(argList) < 2 or len(argList) > 2:
    print('connectz.py: Provide one input file')
    sys.exit(-1)

b = Board()
moves = b.load_file(argList[1])
b.init_board()

# A game is illegal if z is greater than x, y or both
if b.z > b.x or b.z > b.y:
    print(str(7)) # Illegal game

b.play_moves(moves)
win, player = b.checkForZ()

if not win:
    for row in range(len(b.matrix)):
        if 0 in b.matrix[row]:
            print(str(3)) # Incomplete game
            exit(3)
    print(str(0)) # Draw
else:
    print(str(player))
# ----------------------------END---------------------------------