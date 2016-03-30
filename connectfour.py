__author__ = 'Projectgroep Nao7 2015'

from game import *


# Main methode voor het starten van het programma
def main():

    # Maak het spel aan
    g = Game()

    # Begin spel, print het bord
    g.print_state()

    # Speel het spel zolang er geen winnaar is
    while not g.finished:
        g.next_move()

# Start de mainmethode op
if __name__ == "__main__":
    main()