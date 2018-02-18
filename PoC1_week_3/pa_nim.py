"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
# import codeskulptor

# codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000


def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    moves = range(1, MAX_REMOVE + 1)
    best_move = 1
    best_share = 0
    for initial_move in moves:
        num_wins = 0
        for trial in xrange(TRIALS):
            value = initial_move
            victory = True
            while value < num_items:
                value += random.choice(moves)
                victory = not victory
            num_wins += victory
        share = num_wins / float(TRIALS)
        if share > best_share:
            best_share = share
            best_move = initial_move
    return best_move


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """

    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move "))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(10)



