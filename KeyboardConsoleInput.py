'''
KeyboardConsoleInput.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''


from ASCIIDisplay import ASCIIDisplay


class KeyboardConsoleInput:
    @staticmethod
    def read_spacing():
        return int(input("Please choose the board spacing: "))

    @staticmethod
    def read_move(col):
        while True:
            try:
                move = int(input())
                if move < 1 or move > col:
                    raise ValueError
                else:
                    return move-1
            except ValueError:
                ASCIIDisplay.invalid_move_out_of_bounds()
                continue

    @staticmethod
    def read_play_again():
        while True:
            user_input = input()
            if user_input[0] == 'y':
                return True
            elif user_input[0] == 'n':
                return False
