import math

from yahtzee import gen_all_sequences


def task1():
    '''
    Given the set of outcomes corresponding to a coin flip, {Heads,Tails},
    how many sequences of outcomes of length five (repetition allowed) are possible?
    '''
    len_outcome = 5
    elements = {'Heads', 'Tails'}
    num_enum = len(elements) ** len_outcome
    return num_enum


def task2():
    '''
    Consider a sequence of trials in which a fair four-sided die
    (with faces numbered 1-4) is rolled twice. What is the expected value
    of the product of the two die rolls?
    Enter the answer as a floating point number below.
    '''
    outcomes = range(1, 5)
    len_result = 2
    all_seq = gen_all_sequences(outcomes, len_result)
    expected = 0
    len_all_seq = len(all_seq)
    for seq in all_seq:
        expected += (seq[0] * seq[1]) / float(len_all_seq)
    return expected


def task3():
    '''
    Given a trial in which a decimal digit is selected from the list
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] with equal probability 0.1,
    consider a five-digit string created by a sequence of such trials
    (leading zeros and repeated digits are allowed).
    What is the probability that this five-digit string
    consists of five consecutive digits in either ascending or descending order
    (e.g; "34567" or "43210") ?
    Enter your answer as a floating point number
    with at least four significant digits of precision.
    '''
    outcomes = range(10)
    len_result = 5
    all_seq = gen_all_sequences(outcomes, len_result)
    num_consecutive = 0
    len_all_seq = len(all_seq)
    for seq in all_seq:
        gaps = list()
        for idx in xrange(len(seq)):
            try:
                next_val = seq[idx + 1]
                gaps.append(next_val - seq[idx])
            except IndexError:
                break
        if all(i == 1 for i in gaps) or all(i == -1 for i in gaps):
            num_consecutive += 1
    probability = num_consecutive / float(len_all_seq)
    return probability


def task4():
    '''
    Consider a trial in which five digit strings are formed as permutations of the digits
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].
    (In this case, repetition of digits is not allowed.)
    If the probability of each permutation is the same,
    what is the probability that this five digits string consists of
    consecutive digits in either ascending or descending order
    (e.g; "34567" or "43210") ?
    Enter your answer as a floating point number
    with at least four significant digits of precision.
    '''
    size = 10
    length = 5
    num_permutations = math.factorial(size) / float(math.factorial(size - length))
    print num_permutations
    probability = 12 / num_permutations  # see num_consecutive, task3()
    return probability


def task5():
    '''
    Starting from this program template,
    http://www.codeskulptor.org/#poc_permutations_template.py
    implement a function gen_permutations(outcomes, num_trials)
    that takes a list of outcomes and a number of trials
    and returns a set of all possible permutations of length num_trials
    (encoded as tuples) from this set of outcomes.

    Hint: gen_permutations can be built from gen_all_sequences
    by adding a single if statement that prevents repeated outcomes.
    When you believe that your code works correctly, select the answer printed at the bottom of the console.
    '''

    def gen_permutations(outcomes, length):
        answer_set = set([()])
        for dummy_idx in range(length):
            temp_set = set()
            for partial_sequence in answer_set:
                for item in outcomes:
                    new_sequence = list(partial_sequence)
                    if all(new_sequence.count(i) == 1 for i in new_sequence):
                        new_sequence.append(item)
                        temp_set.add(tuple(new_sequence))
            answer_set = temp_set
        return answer_set

    outcome = set(["a", "b", "c", "d", "e", "f"])
    permutations = gen_permutations(outcome, 4)
    permutation_list = list(permutations)
    permutation_list.sort()
    return "Answer is {}".format(permutation_list[100])


def task6():
    '''
    A set S is a subset of another set T if every element x in S is also a member of T.
    Which of the following sets are subsets of the set {1,2}?
    '''
    choices = {'{}': set(),
               '{1,2,3,4}': {1, 2, 3, 4},
               '{1,2}': {1, 2},
               '{3,4}': {3, 4},
               '{2}': {2}}
    target_set = {1, 2}
    subsets = ''
    for option in choices:
        if (choices[option] | target_set) == target_set:
            subsets += option + '\n'
    return subsets


def task7():
    '''
    If the set T has n members, how many distinct sets S are subsets of T?
    You may want to figure out the answer for a few specific values of n first.
    Enter the answer below as a math expression in n.
    '''
    return '2^n'


def task8():
    '''
    Given a standard 52 card deck of playing cards,
    what is the probability of being dealt a five card hand
    where all five cards are of the same suit?
    Hint: Use the formula for combinations to compute the number
    of possible five card hands when the choice of cards
    is restricted to a single suit versus when the choice of cards is unrestricted.
    Compute your answer in Python using math.factorial
    and enter the answer below as a floating point number
    with at least four significant digits of precision.
    '''
    total = 52
    in_one_suit = 13
    length = 5
    all_combinations = (math.factorial(total)) / math.factorial(total - length) * math.factorial(length)
    for_one_suit = (math.factorial(in_one_suit)) / math.factorial(in_one_suit - length) * math.factorial(length)
    relation = for_one_suit / float(all_combinations)
    return relation


def task9():
    '''
    Pascal's triangle is a triangular array of numbers
    in which the entry on one row of the triangle corresponds
    to the sum of the two entries directly above the entry.
    http://en.wikipedia.org/wiki/Pascal's_triangle
    This program prints out the first few rows of Pascal's triangle.
    http://www.codeskulptor.org/#poc_pascal.py
    Enter a math expression in m and n using factorial (!)
    that represents the value of the nth entry of the mth row of Pascal's triangle.
    (Both the row numbers and entry numbers are indexed starting at zero.)
    '''
    def get_value(m_row, n_col):
        value = math.factorial(m_row) / (math.factorial(n_col) * math.factorial(m_row - n_col))
        return value
    expression = 'm!/(n!*(m-n)!)'
    return expression


def task10():
    TEST_CASES = [[0, 0, 0, 0, 4], [0, 0, 0, 0, 10],
                  [0, 1, 2, 3, 4], [0, 2, 2], [0, 3, 2, 3],
                  [0, 1, 1, 1, 3, 5]]
    return str(TEST_CASES)


if __name__ == '__main__':
    # print 'Task 1:', task1()
    # print '\nTask 2:', task2()
    # print '\nTask 3:', task3()
    # print '\nTask 4:', task4()
    # print '\nTask 5:', task5()
    # print '\nTask 6:\n', task6()
    # print 'Task 7:', task7()
    # print '\nTask 8:', task8()
    # print '\nTask 9:', task9()
    print '\nTask 10:', task10()
