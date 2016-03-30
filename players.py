__author__ = 'Projectgroep Nao7 2015'

from minimax import Minimax


# Userklasse, degene die tegen de robot speelt
class User(object):

    # Constructor
    def __init__(self):
        self.color = "x"
        self.moves = []

    # Methode die een move uitvoert
    def move(self, state):
        print("User's beurt(" + self.color + ")")

        # Vraag om een geldige kolom
        column = None
        while column is None:
            # Probeer input te parsen
            try:
                choice = int(input("Voer uw kolomnummer in: ")) - 1
            except ValueError:
                choice = None

            # Check op een geldige move
            if 0 <= choice <= 6:
                column = choice
            else:
                print("Geen geldige move, probeer opnieuw")

        return column


# Robotklasse, de robot die m.b.v. minimax-algoritme speelt
class Robot(object):

    # Constructor
    def __init__(self):
        self.color = "o"
        self.moves = []
        self.difficulty = 10

    # Methode die een move uitvoert m.b.v minimax-algoritme
    def move(self, state):
        print("Robot's beurt(" + self.color + ")")

        # Voer minimax-algoritme uit
        m = Minimax(state)
        best_move, value = m.best_move(self.difficulty, state, self.color)
        return best_move