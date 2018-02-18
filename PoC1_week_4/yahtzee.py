# TASK: https://www.coursera.org/learn/principles-of-computing-1/supplement/MWNxX/mini-project-description
# OWLTEST: http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_yahtzee_tests.py&urlPylintConfig=poc.pylint_config.py
# TEMPLATE: http://www.codeskulptor.org/#poc_yahtzee_template.py
# RESULT: http://www.codeskulptor.org/#user43_OElJqF5rqu_0.py

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
try:
    import codeskulptor

    codeskulptor.set_timeout(20)
except ImportError:
    pass


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


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    values = set(hand)
    max_score = 0
    for value in values:
        count = hand.count(value)
        curr_score = count * value
        if curr_score > max_score:
            max_score = curr_score
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    expected = 0
    values = range(1, num_die_sides + 1)
    all_sequences = gen_all_sequences(values, num_free_dice)
    num_sequences = float(len(all_sequences))
    for seq in all_sequences:
        hand = tuple(list(held_dice) + list(seq))
        max_score = score(hand)
        expected += max_score / num_sequences
    return expected


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    holds = set()
    values = set(hand)
    count = {value: hand.count(value) for value in values}
    for length in xrange(len(hand) + 1):
        sequences = gen_all_sequences(hand, length)
        for sequence in sequences:
            comparison = [sequence.count(val) <= count[val] for val in values]
            if all(comparison):
                sorted_seq = tuple(sorted(list(sequence)))
                holds.add(sorted_seq)
    print holds
    return holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_expected = 0.0
    best_hold = tuple()
    all_holds = gen_all_holds(hand)
    for hold in all_holds:
        num_free_dice = len(hand) - len(hold)
        expected = expected_value(hold, num_die_sides, num_free_dice)
        if expected > max_expected:
            max_expected = expected
            best_hold = hold
    return (max_expected, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    # hand = (1, 1, 1, 5, 6)
    hand = (1,)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

if __name__ == '__main__':
    run_example()
    # hand = (1, 2, 3)
    # print gen_all_holds(hand)

    # hold = (2,)
    # num_sides = 3
    # free_dice = 2
    # print expected_value(hold, num_sides, free_dice)

    # import poc_holds_testsuite
    # poc_holds_testsuite.run_suite(gen_all_holds)







