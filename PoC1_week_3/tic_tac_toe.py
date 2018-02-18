# OwlTest: http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_tttmc_tests.py&urlPylintConfig=poc.pylint_config.py&imports=%7Bpoc:(poc_ttt_provided,%20poc_ttt_gui)%7D
# poc_ttt_provided: http://www.codeskulptor.org/#poc_ttt_provided.py
# Description: https://www.coursera.org/learn/principles-of-computing-1/supplement/7gPV5/mini-project-description
# Codesculptor url: http://www.codeskulptor.org/#user43_NlsteiqDfo_0.py
"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_provided as provided
try:
    import poc_ttt_gui
except ImportError:
    pass

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    '''
    Play a game starting with the given player by making random moves, alternating between players
    '''
    win = board.check_win()
    while win is None:
        empty_squares = board.get_empty_squares()
        tile = random.choice(empty_squares)
        board.move(tile[0], tile[1], player)
        win = board.check_win()
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    Score the completed board and update the scores grid
    '''
    winner = board.check_win()
    if winner == player:
        for row in xrange(len(scores)):
            for col in xrange(len(scores[row])):
                value = board.square(row, col)
                if value == player:
                    scores[row][col] += SCORE_CURRENT
                elif value == provided.EMPTY:
                    scores[row][col] += 0
                else:
                    scores[row][col] -= SCORE_OTHER
    elif winner != player and winner != provided.DRAW:
        for row in xrange(len(scores)):
            for col in xrange(len(scores[row])):
                value = board.square(row, col)
                if value == player:
                    scores[row][col] -= SCORE_CURRENT
                elif value == provided.EMPTY:
                    scores[row][col] += 0
                else:
                    scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    '''
    Find all of the empty squares with the maximum score and randomly return one of them as a (row, column) tuple
    '''
    best_score = - float('Inf')
    best_move = None
    empty = board.get_empty_squares()
    for square in empty:
        if scores[square[0]][square[1]] > best_score:
            best_score = scores[square[0]][square[1]]
            best_move = square
    return best_move


def mc_move(board, player, trials):
    '''
    Use the Monte Carlo simulation described above to return a move for the machine player
    '''
    if len(board.get_empty_squares()):
        dim = board.get_dim()
        scores_map = [[0 for dummy_col in xrange(dim)] for dummy_row in xrange(dim)]
        for dummy_trial in xrange(trials):
            cloned_board = board.clone()
            mc_trial(cloned_board, player)
            mc_update_scores(scores_map, cloned_board, player)
        best_move = get_best_move(board, scores_map)
        return best_move


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)