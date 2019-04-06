'''
GameController.py
Name: Harshil Patel
netID: hpate86
UIN: 670390370
Date: 04/01/2019
'''


from Board import Board
from Player import Player
from KeyboardConsoleInput import KeyboardConsoleInput
from ASCIIDisplay import ASCIIDisplay


class ConnectFourRunner:
    def __init__(self, display):
        self.displayDriver = display         # Display Drivers
        self.b = Board()                     # Instance of Board
        self.players = []                    # List of players
        p1 = Player(22, 1, "R", "Player 1")  # For now 2 players are hard coded,
        p2 = Player(22, 2, "B", "Player 2")  # but in future this game can have many players
        self.players.append(p1)              # added to the list of players Player 1 then Player 2
        self.players.append(p2)
        self.current_move = -1

    # For future changes
    def reinitialize(self, display):
        pass

    # sub method of play_game method
    def player_turn(self, counter, player):
        while True:
            self.displayDriver.prompt_for_move(counter, player.playerName, player.pieceMarker)
            move = KeyboardConsoleInput.read_move(self.b.cols)
            self.current_move = move
            flag = self.b.make_move(move, player)
            if flag:
                return
            else:
                continue

    def check_if_winner(self, player):
        if self.b.check_if_winner(self.current_move, player):
            ASCIIDisplay.win_msg(player.playerName)
            return True
        else:
            return False

    # Play Game method
    def play_game(self):
        turn_counter = 1
        self.displayDriver.printState(self.b)

        while True:
            # Each Player gets their turn
            for p in range(0, len(self.players)):
                # check if game was draw
                if turn_counter == 43:
                    ASCIIDisplay.draw_msg()
                    if KeyboardConsoleInput.read_play_again():
                        return True
                    else:
                        return False
                ConnectFourRunner.player_turn(self, turn_counter, self.players[p])
                self.displayDriver.printState(self.b)
                if ConnectFourRunner.check_if_winner(self, self.players[p]):
                    if KeyboardConsoleInput.read_play_again():
                        return True
                    else:
                        return False
                turn_counter += 1
