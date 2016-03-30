__author__ = 'Projectgroep Nao7 2015'

import random


# Klasse die het algoritme bevat voor de robot
class Minimax(object):
    # Kleuren van de spelers
    colors = ["x", "o"]

    # Constructor
    def __init__(self, board):
        # Kopieer het huidige bord
        self.board = [x[:] for x in board]

    # Methode die de beste move voor de robot berekend
    def best_move(self, depth, state, curr_player):
        # Bepaal de kleur van de tegenstander
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        # Loop over alle geldige moves
        legal_moves = {}
        for col in xrange(7):
            # Voeg de move uit als deze binnen het bord past
            if self.is_legal_move(col, state):
                temp = self.make_move(state, col, curr_player)
                legal_moves[col] = -self.search(depth - 1, temp, opp_player)

        best_alpha = -99999999
        best_move = None
        moves = legal_moves.items()
        random.shuffle(moves)
        for move, alpha in moves:
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

        return best_move, best_alpha

    # Methode die naar geldige moves zoekt
    def search(self, depth, state, curr_player):
        # Loop over alle geldige moves
        legal_moves = []
        for i in xrange(7):
            # Voeg de move uit als deze binnen het bord past
            if self.is_legal_move(i, state):
                temp = self.make_move(state, i, curr_player)
                legal_moves.append(temp)

        # Als einde van het spel bereikt is/wordt
        if depth == 0 or len(legal_moves) == 0 or self.game_is_over(state):
            return self.value(state, curr_player)

        # Bepaal verschillende kleuren
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        alpha = -99999999
        for child in legal_moves:
            if child is None:
                print("Geen kind gevonden")
            alpha = max(alpha, -self.search(depth - 1, child, opp_player))
        return alpha

    # Methode die checkt of de move past in het bord
    def is_legal_move(self, column, state):
        # Checkt op een lege plek in de kolom
        for i in xrange(6):
            if state[i][column] == ' ':
                return True

        # Geen plek gevonden
        return False

    # Methode die
    def game_is_over(self, state):
        if self.check_for_streak(state, self.colors[0], 4) >= 1:
            return True
        elif self.check_for_streak(state, self.colors[1], 4) >= 1:
            return True
        else:
            return False

    # Methode die een kopie maakt van het bord met de nieuwe move
    def make_move(self, state, column, color):
        temp = [x[:] for x in state]
        for i in xrange(6):
            if temp[i][column] == ' ':
                temp[i][column] = color
                return temp

    # Methode die mogelijke move waardeert
    def value(self, state, color):
        if color == self.colors[0]:
            o_color = self.colors[1]
        else:
            o_color = self.colors[0]

        my_fours = self.check_for_streak(state, color, 4)
        my_threes = self.check_for_streak(state, color, 3)
        my_twos = self.check_for_streak(state, color, 2)
        opp_fours = self.check_for_streak(state, o_color, 4)

        if opp_fours > 0:
            return -100000
        else:
            return my_fours * 100000 + my_threes * 100 + my_twos

    # Methode die het aantal mogelijkheden op vier op een rij telt
    def check_for_streak(self, state, color, streak):
        count = 0

        # Check voor alle mogelijkheden in het bord
        for i in xrange(6):
            for j in xrange(7):

                # Check op kleur van de robot
                if state[i][j].lower() == color.lower():
                    # Voeg aantal mogelijkheden op vier op een rij toe
                    count += self.vertical_streak(i, j, state, streak)
                    count += self.horizontal_streak(i, j, state, streak)
                    count += self.diagonal_check(i, j, state, streak)

        return count

    # Methode die mogelijkheden geeft op een verticale vier op een rij
    def vertical_streak(self, row, col, state, streak):
        consecutive_count = 0
        for i in xrange(row, 6):
            if state[i][col].lower() == state[row][col].lower():
                consecutive_count += 1
            else:
                break

        if consecutive_count >= streak:
            return 1
        else:
            return 0

    # Methode die mogelijkheden geeft op een horizontale vier op een rij
    def horizontal_streak(self, row, col, state, streak):
        consecutive_count = 0
        for j in xrange(col, 7):
            if state[row][j].lower() == state[row][col].lower():
                consecutive_count += 1
            else:
                break

        if consecutive_count >= streak:
            return 1
        else:
            return 0

    # Methode die mogelijkheden geeft op een diagonale vier op een rij
    def diagonal_check(self, row, col, state, streak):
        # Totaal aan mogelijkheden
        total = 0

        # Check voor stijgende diagonaal
        consecutive_count = 0
        j = col
        for i in xrange(row, 6):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                consecutive_count += 1
            else:
                break
            j += 1

        if consecutive_count >= streak:
            total += 1

        # Check voor dalende diagonaal
        consecutive_count = 0
        j = col
        for i in xrange(row, -1, -1):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                consecutive_count += 1
            else:
                break
            j += 1

        if consecutive_count >= streak:
            total += 1

        return total

