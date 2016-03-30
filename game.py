__author__ = 'Projectgroep Nao7 2015'

import random
from players import *


# Gameklasse voor vier op een rij
class Game(object):
    # Constructor
    def __init__(self):
        # Statistieken
        self.round = 1
        self.finished = False
        self.winner = None

        # Speler en robot
        self.players = [User(), Robot()]

        # Tos voor beginnende speler
        tos = random.random()
        if tos < 0.5:
            self.turn = self.players[0]
        else:
            self.turn = self.players[1]

        # Creer het bord
        """
        self.board = [
        ['o', 'x', 'o', '', 'x', 'o', 'x'],
        ['o', 'o', 'x', '', 'x', 'x', 'x'],
        ['o', 'o', 'x', '', 'o', 'o', 'o'],
        ['x', 'o', 'x', '', 'x', 'o', 'x'],
        [' ', 'x', 'o', '', 'x', 'o', ' '],
        [' ', 'x', 'o', '', 'o', 'x', ' ']
        ]
        """

        self.board = []
        for i in xrange(6):
            self.board.append([])
            for j in xrange(7):
                self.board[i].append(' ')

        # Lijst met moves
        self.usermoves = []
        self.playermoves = []

    # Methode die de beurt switch tussen robot en user
    def switch_turn(self):
        if self.turn == self.players[0]:
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]

        self.round += 1

    # Methode die de volgende zet uitvoert
    def next_move(self):

        # Speler die aan de beurt is
        player = self.turn

        # Checkt of het bord vol is (ronde 42)
        if self.round > 42:
            self.finished = True
            return

        # Speler voert het kolomnummer in
        move = player.move(self.board)

        # Checkt voor de eerste lege plek in de kolom
        for i in xrange(6):
            if self.board[i][move] == ' ':
                # Voeg toe aan historie
                player.moves.append([i, move])

                self.board[i][move] = player.color
                self.switch_turn()

                if self.check_winner(player.moves):
                    self.winner = player
                    self.finished = True

                #self.check_for_fours()
                self.print_state()
                return

        # Kolom is vol
        print("Ongeldige move (kolom is vol)")
        return

    # Methode om de lijsten te sorteren om te checken op vier op een rij
    def check_winner(self, list):
        # counter voor opvolgende discs
        last_row = -10
        last_column = -10
        total = -10

        # sorteer op kolom
        list.sort()

        # loop verticaal over de list
        counter = 0
        for move in list:
            # als opeenvolgend dan counter verhogen en index onthouden
            if move[1] - last_column is 1 and move[0] is last_row:
                counter += 1

                # check of 4 disc connected zijn
                if counter is 4:
                    print "Er is verticaal 4 op een rij"
                    return True
            # anders counter resetten
            else:
                last_row = move[0]
                counter = 1

            # laatste kolom onthouden
            last_column = move[1]

        # sorteer op rij
        list.sort(key=lambda move: move[1])

        # loop horizontaal over de list
        counter = 0
        for move in list:
            # als opeenvolgend dan counter verhogen en index onthouden
            if move[0] - last_row is 1 and move[1] is last_column:
                counter += 1

                # check of 4 disc connected zijn
                if counter is 4:
                    print "Er is horizontaal 4 op een rij"
                    return True

            # anders counter resetten
            else:
                last_column = move[1]
                counter = 1

            # last row onthouden
            last_row = move[0]

        # sorteer op boven/onder diagonaal
        list.sort(key=lambda move: move[0] + move[1])

        # loop diagonaal over de lijst
        counter = 0
        for move in list:
            if move[0] + move[1] is total:
                counter += 1

                # check of 4 disc connected zijn
                if counter is 4:
                    print "Er is schuin van boven naar onder 4 op een rij"
                    return True
            else:
                total = move[0] + move[1]
                counter = 1

        # sorteer op onder/boven diagonaal
        list.sort(key=lambda move: move[0] - move[1])

        # loop diagonaal over de lijst
        counter = 0
        for move in list:
            if move[0] - move[1] is total:
                counter += 1

                # check of 4 disc connected zijn
                if counter is 4:
                    print "Er is schuin van onder naar boven 4 op een rij"
                    return True
            else:
                total = move[0] - move[1]
                counter = 1
        return False

    # Methode om het bord mee te printen
    def print_state(self):
        # Print het ronde nummer
        print("Ronde: " + str(self.round))

        # Print de het spelbord
        for i in xrange(5, -1, -1):
            print("\t"),
            for j in xrange(7):
                print("| " + str(self.board[i][j])),
            print("|")
        print("\t  _   _   _   _   _   _   _ ")
        print("\t  1   2   3   4   5   6   7 ")

        # Print de winnaar bij einde spel
        if self.finished:
            print("Het spel is afgelopen!")

            # Check winnaar
            if self.winner is not None:
                if isinstance(self.winner, User):
                    print("User is de winnaar")
                else:
                    print("Robot is de winnaar")
            else:
                print("Er is een gelijkspel")