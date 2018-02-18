# POC 1, Week 0
# Practice Mini-project: Solitaire Mancala
# CodeSculptor URL: http://www.codeskulptor.org/#user42_DgwgSXIUwO_0.py


"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = []

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = configuration[:]

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        output = self._board[:]
        output.reverse()
        return str(output)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return sum(self._board[1:]) == 0

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return self._board[house_num] == house_num and house_num != 0

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for index in xrange(self._board[house_num]):
                self._board[house_num - index - 1] += 1
            self._board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        village = self._board[1:]
        for index in xrange(len(village)):
            if self.is_legal_move(index + 1):
                return index + 1
        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
		After each move, move the seeds in the house closest to the store
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        simulator = self._board[:]
        game_on = True
        results = list()
        move = 0
        while game_on:
            for index in xrange(len(simulator)):
                if index != 0 and simulator[index] == index:
                    move = index
                    results.append(move)
                    break
            else:
                game_on = False
            if move != 0:
                for step in xrange(simulator[move]):
                    simulator[move - step - 1] += 1
                simulator[move] = 0
        return results


def test_mancala():
    """
    Test code for Solitaire Mancala
    """


    # my_game2 = SolitaireMancala()
    # my_game3 = SolitaireMancala()
    # print "Testing init - Computed:", my_game, "Expected: [0]"

    # config1 = [0, 0, 1, 1, 3, 5, 0]
    # my_game.set_board(config1)
    #
    # config2 = [10, 0, 0, 0, 0, 0, 0]
    # my_game2.set_board(config2)
    #
    # config3 = [0, 3, 2, 0, 0]
    # my_game3.set_board(config3)

    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    #
    # print 'Testing is_game_won - Computed:', my_game.is_game_won(), 'Expected: False'
    # print 'Testing is_game_won - Computed:', my_game2.is_game_won(), 'Expected: True'



    # print 'my_game3', str(my_game3)
    # print 'Testing is_legal_move - Computed:', my_game3.is_legal_move(1), 'Expected: False'
    # print my_game3.get_num_seeds(1), 'Expected:', config3[1]
    # print 'Testing is_legal_move - Computed:', my_game3.is_legal_move(2), 'Expected: True'
    # print my_game3.get_num_seeds(2), 'Expected:', config3[2]
    # print 'Testing is_legal_move - Computed:', my_game3.is_legal_move(3), 'Expected: False'
    # print my_game3.get_num_seeds(3), 'Expected:', config3[3]

    # print 'Test apply_move'
    # my_game.apply_move(5)
    # result = [1, 1, 2, 2, 4, 0, 0]
    # result.reverse()
    # print 'Test apply_move - Computed:', str(my_game), 'Expexted:', str(result)
    # my_game.apply_move(1)
    # result = [2, 0, 2, 2, 4, 0, 0]
    # result.reverse()
    # print 'Test apply_move - Computed:', str(my_game), 'Expexted:', str(result)
    # my_game.apply_move(2)
    # result = [3, 1, 0, 2, 4, 0, 0]
    # result.reverse()
    # print 'Test apply_move - Computed:', str(my_game), 'Expexted:', str(result)

    # print 'Test choose_move'
    # print 'my_game', str(my_game)
    # num = my_game.choose_move()
    # print 'Test choose_move - Computed:', num, 'Expected', 2
    # print my_game.get_num_seeds(num)
    # print 'my_game2', str(my_game2)
    # num = my_game2.choose_move()
    # print 'Test choose_move - Computed:', num, 'Expected', 0
    # print my_game2.get_num_seeds(num)
    # print 'my_game3', str(my_game3)
    # num = my_game3.choose_move()
    # print 'Test choose_move - Computed:', num, 'Expected', 2
    # print my_game3.get_num_seeds(num)

    # print 'Test plan_moves'
    # print 'Test plan_moves - Computed', my_game.plan_moves(), 'Expected: [2, 1, 3, 2, 1, 4, 1, ...]'

    # print 'Testing choose_move() and apply_move() on configuration [0, 0, 0, 0, 2, 4, 6]'
    # my_game4 = SolitaireMancala()
    # config4 = [0, 0, 0, 0, 2, 4, 6]
    # my_game4.set_board(config4)
    # print str(my_game4)
    # move = my_game4.choose_move()
    # print 'house', move
    # my_game4.apply_move(move)
    # print str(my_game4)

    # my_game6 = SolitaireMancala()
    # config6 = [0, 1, 2, 3]
    # my_game6.set_board(config6)
    # print my_game6
    # move = my_game6.choose_move()
    # print 'house', move
    # my_game6.apply_move(move)
    # print my_game6
    # move = my_game6.choose_move()
    # print 'house', move
    # my_game6.apply_move(move)
    # print my_game6

    #
    # my_game5 = SolitaireMancala()
    # # config5 = [10, 2, 3, 4]
    # config5 = [0, 0, 0, 0, 10]
    # print 'Testing plan_moves() on configuration', str(config5)
    # my_game5.set_board(config5)
    # print my_game5.plan_moves()


test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())