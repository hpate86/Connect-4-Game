'''
Player.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''


from Piece import Piece
from ASCIIDisplay import ASCIIDisplay


class Player:
    def __init__(self, number_of_piece, player_number=-1, piece_marker="?", player_name="Unknown"):
        self.playerNumber = player_number
        self.pieceMarker = piece_marker
        self.playerName = player_name
        self.pieces = []
        for p in range(0, number_of_piece):
            pi = Piece(-1, -1, piece_marker)
            self.pieces.append(pi)

    # sent the next available piece of the player
    def get_piece_to_add(self):
        for p in self.pieces:
            if p.col == -1 and p.row == -1:
                return p
        ASCIIDisplay.piece_limit_error()

    # sent the last move done by the player sent only ROW
    def get_last_move_row(self):
        for p in range(0, len(self.pieces)):
            if self.pieces[p].col == -1 and self.pieces[p].row == -1:
                return self.pieces[p-1].row
