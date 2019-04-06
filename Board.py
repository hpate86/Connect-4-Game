'''
Board.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''

from Cell import Cell
from ASCIIDisplay import ASCIIDisplay
# from Piece import Piece
# from Piece import Piece

'''
    Col by row 
     x  by  y 
'''

class Board:
    '''A container for the collection of spaces in the playing field'''
    def __init__(self, col=7, row=6, connect=5):
        '''Tic Tac Toe defaults to a 3 by 3 board

        cells is a 2 dimensional list of cell objects
        The first list is the list of columns
        Each column contains a list of rows
        How you construct your board is up to you, just be consistent'''
        self.connect = connect
        self.rows = row
        self.cols = col
        self.cells = []
        for cell_col in range(self.cols):
            new_row = []
            for cell_row in range(self.rows):
                new_row.append(Cell(cell_col, cell_row))
            self.cells.append(new_row)

    def add_piece(self, col, row, p):
        '''Give the column and row of a piece to be placed absolutely

        For tic tac toe, we used this method instead of move piece.
        Normally one would probably check whether the position was occupied and
            potentially do something different if so.'''
        # return self.cells[row][col].update(p)
        pi = p.get_piece_to_add()
        pi.make_move(col, row, self)

        self.cells[col][row].piece = pi
        self.cells[col][row].occupied = True
        #pi._printInfo()

    def make_move(self, x, p):
        '''Give the column to drop and the piece to be dropped into the board

            Should engage the physics logic of the cells'''
        if not self.cells[x][self.rows-1].empty():
            ASCIIDisplay.col_full_error(x)
            return False

        for y in range(self.rows):
            if self.cells[x][y].empty():
                Board.add_piece(self, x, y, p)
                return True
            else:
                continue

    def move_piece(self, origCol, origRow, col, row, p):
        pass

    # sub method for check_if_win - Vertical
    def check_vertical(self, col, row, p):
        '''For a given col, check there are enough cells below the current cell
            to check, because in connect 4, there must be other 3 cell below the
            current cell for that player to at least consider winning with
            vertical row match. In sort from the current cell, check the bottom
            3 piece marker if they are the same then player has won
        '''
        if row > self.connect - 2:
            for i in range(0, self.connect):
                if p.pieceMarker == self.cells[col][row].piece.disp:
                    row -= 1
                    if i == self.connect - 1:
                        return True
                    continue
                else:
                    break

    # sub method for check_if_win - Horizontal
    def check_horizontal(self, col, row, p):
        count = 0
        for c in range(0, self.cols):
            if not self.cells[c][row].piece is None:
                if p.pieceMarker == self.cells[c][row].piece.disp:
                    if count == self.connect-1:
                        return True
                    count += 1
                else:
                    count = 0
            else:
                count = 0

    def check_diagonal(self, col, row, p):
        # Bottom left to top right
        for colStart in range(0, (self.cols-(self.connect-1))):
            count = 0
            c = colStart
            r = 0
            while c < self.cols and r < self.rows:
                if not self.cells[c][r].piece is None:
                    if p.pieceMarker == self.cells[c][r].piece.disp:
                        if count == self.connect-1:
                            return True
                        count += 1
                    else:
                        count = 0
                else:
                    count = 0
                c += 1
                r += 1

        for rowStart in range(1, (self.rows - (self.connect - 1))):
            count = 0
            c = 0
            r = rowStart
            while c < self.cols and r < self.rows:
                if not self.cells[c][r].piece is None:
                    if p.pieceMarker == self.cells[c][r].piece.disp:
                        if count == self.connect-1:
                            return True
                        count += 1
                    else:
                        count = 0
                else:
                    count = 0
                c += 1
                r += 1

        # top left to bottom right
        for colStart in range(0, (self.cols-(self.connect-1))):
            count = 0
            c = colStart
            r = self.rows-1
            while c < self.cols and r >= 0:
                if not self.cells[c][r].piece is None:
                    if p.pieceMarker == self.cells[c][r].piece.disp:
                        if count == self.connect - 1:
                            return True
                        count += 1
                    else:
                        count = 0
                else:
                    count = 0
                c += 1
                r -= 1

        for rowStart in range(self.rows-2, (self.rows - self.connect), -1):
            count = 0
            c = 0
            r = rowStart
            while c < self.cols and r >= 0:
                if not self.cells[c][r].piece is None:
                    if p.pieceMarker == self.cells[c][r].piece.disp:
                        if count == self.connect-1:
                            return True
                        count += 1
                    else:
                        count = 0
                else:
                    count = 0
                c += 1
                r -= 1

    def check_if_winner(self, col, p):
        '''Get the Row coordinate of the players most recent move'''
        row = p.get_last_move_row()

        if Board.check_vertical(self, col, row, p) or Board.check_horizontal(self, col, row, p) or Board.check_diagonal(self, col, row, p):
            return True
        else:
            return False
