'''
Piece.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''


class Piece:
    def __init__(self, col=-1, row=-1, piece_symbol='&', b=None):
        self.col = col
        self.row = row
        self.disp = piece_symbol
        self.board = b

    #@abc.abstractmethod
    def validate_move(self, col, row, b):
        pass

    #@abc.abstractmethod
    def make_move(self, col, row, b):
        self.col = col
        self.row = row
        self.board = b

    # def debug_string(self):
    #     if(debug_flag):
    #         return self._printInfo()
    #     return ""

    def _printInfo(self):
        s = "col: " + str(self.col) + "\nrow: " + str(self.row) + "\ntype of piece: " + self.disp
        print(s)
        return s

    def __str__(self):
        return self.disp


# class ConnectFourPiece(Piece):
#     # def __init__(self, player, col=-1, row=-1, piece_symbol='&'):
#     def __init__(self, col=-1, row=-1, piece_symbol='&'):
#         super().__init__(col, row, piece_symbol)
#
#     def set_location(self, loc):
#         pass
#
#     def validate_move(self, x, y):
#         pass
#
#     def make_move(self, x, y, b):
#         super().make_move(x, y, b)
#         pass
#
#     def _printInfo(self): # Unnecessary as of now
#         super()._printInfo()