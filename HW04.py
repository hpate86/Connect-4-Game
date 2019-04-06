'''
HW04.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''


from ASCIIDisplay import ASCIIDisplay
from GameController import ConnectFourRunner
from KeyboardConsoleInput import KeyboardConsoleInput
debug_flag = False

if __name__ == "__main__":

    user_spacing = KeyboardConsoleInput.read_spacing()
    d = ASCIIDisplay(user_spacing) # display driver
    # d.printState(b)
    r = ConnectFourRunner(d)
    while r.play_game():
        d = ASCIIDisplay(user_spacing)
        r = ConnectFourRunner(d)
    ASCIIDisplay.byee()
