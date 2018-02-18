# POC 1, Week 0
# Practice Mini-project: Solitaire Mancala
# CodeSculptor URL: http://www.codeskulptor.org/#user42_DgwgSXIUwO_0.py


"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

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

    def alt_plan_moves(self):
        """
        Simulator for tweaks
        """
        ret = []
        while not self.is_game_won():
            check_num = self.choose_move()
            if check_num != 0:
                ret.append(check_num)
            if check_num == 0:
                break
            self.apply_move(check_num)
        return ret


class SolitaireMancala2:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for idx in range(1, len(self._board)):
            if self._board[idx] != 0:
                return False
        return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        move_in_range = 0 < house_num < len(self._board)
        index_matches = self._board[house_num] == house_num
        return move_in_range and index_matches

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for idx in range(house_num):
                self._board[idx] += 1
            self._board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in range(1, len(self._board)):
            if self.is_legal_move(house_num):
                return house_num
        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
        After each move, move the seeds in the house closest to the store
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        new_board = SolitaireMancala()
        new_board.set_board(self._board)
        move_list = []
        next_move = new_board.choose_move()
        while next_move != 0:
            new_board.apply_move(next_move)
            move_list.append(next_move)
            next_move = new_board.choose_move()
        return move_list


class OtherMancala37():
    def __init__(self):
        self.game_board = [0]

    def set_board(self, configuration):
        self.game_board = configuration[::]

    def __str__(self):
        game_board = self.game_board[::]
        game_board.reverse()
        return str(game_board)

    def get_num_seeds(self, house_num):
        return self.game_board[house_num]

    def is_game_won(self):
        if (self.game_board[1:].count(0) == len(self.game_board[1:])):
            return True
        return False

    def is_legal_move(self, house_num):
        if (house_num == 0):
            return False
        elif (self.game_board[house_num] == house_num):
            return True
        return False

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            self.game_board[house_num] = 0
            for num in range(house_num):
                self.game_board[num] += 1

    def choose_move(self):
        for num in self.game_board[1:]:
            if (self.game_board.index(num, 1) == num):
                return num
        return 0

    def plan_moves(self):
        ret = []
        while (not self.is_game_won()):
            check_num = self.choose_move()
            if (check_num != 0):
                ret.append(check_num)
            if (check_num == 0):
                break
            self.apply_move(check_num)
        return ret


class OtherMancala41():
    def __init__(self):
        self._board = [0]

    def set_board(self, configuration):
        self._board = configuration[:]

    def __str__(self):
        return str([self._board[i] for i in range((len(self._board) - 1), (-1), (-1))])

    def get_num_seeds(self, house_num):
        return self._board[house_num]

    def is_legal_move(self, house_num):
        if ((house_num == 0) or (house_num >= len(self._board))):
            return False
        else:
            return (house_num == self._board[house_num])

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for i in range(house_num):
                self._board[i] += 1
            self._board[house_num] = 0

    def choose_move(self):
        for i in self._board[1:]:
            if self.is_legal_move(i):
                return i
        return 0

    def is_game_won(self):
        won = True
        for i in self._board[1:]:
            if (i != 0):
                won = False
        return won

    def plan_moves(self):
        moves = []
        while True:
            move = self.choose_move()
            if ((move == 0) or self.is_game_won()):
                break
            else:
                self.apply_move(move)
                moves.append(move)
        return moves


class OtherMancala42():
    def __init__(self):
        self._store = [0]

    def set_board(self, configuration):
        self._store = configuration[:]

    def __str__(self):
        return str(self._store[::(-1)])

    def get_num_seeds(self, house_num):
        return self._store[house_num]

    def is_game_won(self):
        return (sum(self._store[1:]) == 0)

    def is_legal_move(self, house_num):
        return ((house_num == self._store[house_num]) and (house_num > 0))

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for index in range(house_num):
                self._store[index] += 1
            self._store[house_num] = 0

    def choose_move(self):
        move = 0
        for index in range((len(self._store) - 1)):
            if (self.is_legal_move((index + 1)) and (move == 0)):
                move = (index + 1)
        # print move
        return move

    def plan_moves(self):
        moves = []
        count = 0
        temp_store = self._store[:]
        while (count < 10):
            move = self.choose_move()
            if (move > 0):
                moves.append(move)
                self.apply_move(move)
            else:
                break
            count += 1
        self._store = temp_store[:]
        return moves


def find_bug():
    choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    length = 6
    all_seq = gen_all_sequences(choices, length)
    for seq in all_seq:
        if seq[0] == 0:
            game = SolitaireMancala2()
            other = OtherMancala42()
            config = list(seq)
            game.set_board(config)
            other.set_board(config)
            model = game.plan_moves()
            test = other.plan_moves()
            if model != test:
                print 'CONFIG:', config
                print 'expected: {}, received: {}'.format(model, test)
    print 'DONE'


find_bug()

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    for case in [[0, 2, 2]]:
        print case
        my_game = SolitaireMancala2()
        other = OtherMancala37()
        my_game.set_board(case)
        other.set_board(case)
        model = my_game.plan_moves()
        test = other.plan_moves()
        if model != test:
            print 'TESTING plan_moves FOR CONFIG: {}'.format(case)
            print 'EXPECTED: {}, RECEIVED: {}'.format(str(model), str(test))


# test_mancala()
