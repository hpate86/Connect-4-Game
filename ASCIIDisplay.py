'''
ASCIIDisplay.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''


class ASCIIDisplay:
    def __init__(self,spacing = 1):
        self.spacing = spacing

    def printState(self, b):
        fullString = ""
        across = range(0,b.cols)
        #up = range(0, b.rows, 1)
        up = range(b.rows-1,-1,-1)
        spaces = range(self.spacing)
        for i in up:
            top = "+"
            for j in across:
                for k in spaces:
                    top = top + "-"
                top = top + "-"
                for k in spaces:
                    top = top + "-"
                top = top + "+"
            top = top + "\n"
            fullString = fullString + top
            top = "+"
            for j in across:
                for k in spaces:
                    top = top + " "
                top = top + str(b.cells[j][i]) #.piece.disp
                for k in spaces:
                    top = top + " "
                if(j == b.cols):
                    top = top + "+"
                else:
                    top = top + "|"
            top = top + "\n"
            fullString = fullString + top
        top = "+"
        #bottom
        for j in across:
            for k in spaces:
                top = top + "-"
            top = top + "-"
            for k in spaces:
                top = top + "-"
            top = top + "+"
        top = top + "\n"
        fullString = fullString+top
        #indices
        top = " "
        for j in across:
            for k in spaces:
                top = top + " "
            top = top + str(j+1)
            for k in range(self.spacing-len(str(j+1))+1):
                top = top + " "
            top = top + " "
        top = top + "\n"
        fullString = fullString+top
        print(fullString)

    @staticmethod
    def prompt_for_move(turn_count, player_name, player_symbol):
        print("Turn {}: {} ({}), choose your move: ".format(turn_count, player_name, player_symbol), end='')

    @staticmethod
    def invalid_move_out_of_bounds():
        print("Invalid move, outside board, try again: ", end='')

    @staticmethod
    def col_full_error(loc):
        print("Invalid move, column {} is full, try again: ".format(loc+1))

    @staticmethod
    def piece_limit_error():
        print("No more pieces left")

    @staticmethod
    def win_msg(player_name):
        print("{} Wins! Play again? (y/n): ".format(player_name), end='')

    @staticmethod
    def draw_msg():
        print("Game was draw! Play again? (y/n): ", end='')

    @staticmethod
    def byee():
        print("Goodbye!")
