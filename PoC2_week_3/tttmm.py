"""
Mini-max Tic-Tac-Toe Player

TEMPLATE: http://www.codeskulptor.org/#poc_tttmm_template.py
TASK: https://www.coursera.org/learn/principles-of-computing-2/supplement/hPToP/mini-project-description
OWLTEST: http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_tttmm_tests.py&urlPylintConfig=poc.pylint_config.py&imports=%7Bpoc:(poc_ttt_provided,poc_ttt_gui)%7D
IMPLEMENTATION: http://www.codeskulptor.org/#user43_Xqf1u1I7nbkHPt6.py
"""

# import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor

# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win():
        return SCORES[board.check_win()], (-1, -1)
    empty_squares = board.get_empty_squares()
    best = (-1 * SCORES[player], (-1, -1))
    for square in empty_squares:
        cloned_board = board.clone()
        cloned_board.move(square[0], square[1], player)
        next_player = provided.switch_player(player)
        score, dummy_square = mm_move(cloned_board, next_player)
        result = score * SCORES[player]
        print result, square
        if result == 1:
            return score, square
        elif result > best[0] * SCORES[player]:
            best = score, square
    return best


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.


# provided.play_game(move_wrapper, 2, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)


# print mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
#                                            [provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
#                                            [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO)
#
# print mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
#                                            [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
#                                            [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX)