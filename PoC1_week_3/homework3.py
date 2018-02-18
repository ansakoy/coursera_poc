# -*- coding: utf-8 -*-

import random
import math

def task1():
    '''
    What is the sum of the probabilities associated with the all possible outcomes of a single trial?
    '''
    answer = 1
    return answer


def task2():
    '''
    You are dealt a single card from a standard deck of 52 playings cards
    (4 suits with 13 cards in each suit).
    What is the probability that the card will be of a specific suit?
    '''
    answer = 13 / 52.0
    return answer


def task3():
    '''
    Consider a trial with 36 possible outcomes where each outcome has equal probability.
    How many outcomes correspond to an event that has probability 1/9?
    '''
    answer = 36 * (1/9.0)
    return answer


def task4():
    '''
    Which Python expressions below simulate a single trial
    corresponding to the roll of a fair six-sided die
    whose faces are numbered 1 to 6?
    '''
    options = {'random.randrange(1, 7)': range(1, 7),
               'random.randrange(6)': range(6),
               'random.randrange(1, 6)': range(1, 6),
               'random.randrange(6) + 1': [n + 1 for n in range(6)]}
    die_sides = [1, 2, 3, 4, 5, 6]
    results = ''
    for option in options:
        if options[option] == die_sides:
            results += option + '\n'
    return results


def task5():
    '''
    Given a standard deck of 52 cards, what is the probability
    that two cards drawn at random will have the same rank?
    Note that first card drawn is not added back
    into the deck when the second card is drawn.
    '''

    total_cards = 52
    all_ranks = 4
    left_after_first_picked = total_cards - 1
    left_of_the_same_rank = all_ranks - 1
    chance_second_same_rank = left_of_the_same_rank / float(left_after_first_picked)
    return '{}/{} = {}/{} = {}'.format(left_of_the_same_rank,
                                       left_after_first_picked,
                                       left_of_the_same_rank / left_of_the_same_rank,
                                       left_after_first_picked / left_of_the_same_rank,
                                       chance_second_same_rank)


def task6():
    '''
    What is the mean GPA of class where
    30% of the students have 4.0 GPA,
    40% of the students have a 3.0 GPA and
    20% of the students have 2.0 GPA, and
    10% of the student have a 1.0 GPA?
    '''
    mean = 4.0 * .3 + 3.0 * .4 + 2.0 * .2 + 1.0 * 1
    return mean


def task7():
    '''
    Consider a dice game in which you roll two dice.
    If the sum of the dice is odd, you win $1.
    If the sum of the dice is even, you lose $1.
    What is the expected value (in terms of your winnings)
    of a single roll in this game?
    '''
    options = {'positive': 'The expected value is positive. If I play this game a lot, I expect to win money.',
               'zero': 'The expected value is zero. If I play this game a lot, I expect to break even.',
               'negative': 'The expected value is negative. If I play this game a lot, I expect to lose money.'}
    prob_even_sum = .5
    prob_odd_sum = .5
    expected = -1 * prob_even_sum + 1 * prob_odd_sum
    if expected > 0:
        return options['positive']
    elif expected < 0:
        return options['negative']
    else:
        return options['zero']


def task8():
    '''
    What is the expected value of trial(n) as a function of n?
    (Here, assume that n is a positive integer.)
    Enter the answer below as a math expression in n.
    '''

    def trial(n):
        val = random.randrange(n)
        return val

    sum_formula = 'sum(0 + 1 + 2 + ... + k) = 1/2 * k * (k + 1)'
    range_sum_formula = '1/2 * (n - 1) * (n - 1 + 1)'
    simplified_range_sum_formula = '((n - 1) * n) / 2'
    expected = '(((n - 1) * n) / 2) / n = ((n - 1) * n) / 2) * (1 / n)'
    simplified_expected = '((n - 1) * n) / (2 * n)'
    result = '(n - 1) / 2'
    return result


def task9():
    '''
    Consider that following mystery program.
    http://www.codeskulptor.org/#poc_mystery.py
    This program uses random.random() to generate a random set of points
    that are uniformly distributed over the square
    with corners at (1,1), (−1,1), (1,−1), and (−1,−1).
    (Here, being uniformly distribution means that each point in the square
    has an equal chance of being generated.)
    The method then tests whether these points lie inside a unit circle.

    As one increases the number of trials,
    the value returned by estimate_mystery tends towards
    a specific value that has a simple expression involving a well-known constant.

    Enter this value as a math expression below.
    (Do not enter a floating point number.)
    You can consult this page if you would like to see
    a list of math constants that Coursera's quiz system recognizes.
    https://www.coursera.org/learn/principles-of-computing-1/supplement/Ita4e/math-expressions-for-homework
    '''
    def per_cent_circle_area(len_square_side):
        radius = len_square_side / 2
        circle_area = math.pi * radius ** 2
        square_area = len_square_side ** 2
        circle_share = circle_area / square_area
        return circle_share

    circle_share = per_cent_circle_area(2)
    math_expression = 'pi/4'
    return 'Value is {}\nMath expression is {}'.format(circle_share, math_expression)


def task10():
    '''
    OwlTest: http://codeskulptor.appspot.com/owltest/?urlTests=poc.iipp_format_tests_machine.py&urlPylintConfig=skip
    '''

    def format(t):
        # My implementation of the function
        global tens
        tens = t % 10
        sec1 = (t // 10) % 10
        sec10 = t // 10 % 60 // 10
        mins = t // 600
        return str(mins) + ":" + str(sec10) + str(sec1) + "." + str(tens)

    def test_format(t):
        # A random function from OwlTest
        if (t <= 9):
            A = '0'
            B = '0'
            C = '0'
        elif (len(str(t)) == 2):
            A = '0'
            B = '0'
            C = (t // 10)
        else:
            A = (t // 600)
            t = (t % 600)
            if (len(str(t)) == 3):
                B = ((t // 10) // 10)
                C = ((t // 10) % 10)
            elif (len(str(t)) < 3):
                if (t <= 59):
                    B = '0'
                    C = (t // 10)
                else:
                    B = (((t % 60) // 10) % 10)
                    C = (t // 10)
        D = (t % 10)
        return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))

    TEST_CASES = [0, 11, 321, 613, 1000, 700, 2, 10, 670]

    # for case in TEST_CASES:
    #     expected = format(case)
    #     result = test_format(case)
    #     if expected != result:
    #         print 'CASE: {}, expected: {}, actual: {}'.format(case, expected, result)
    return str(TEST_CASES)

if __name__ == '__main__':
    print 'Task 1:', task1()
    print '\nTask 2:', task2()
    print '\nTask 3:', task3()
    print '\nTask 4:\n', task4()
    print 'Task 5:', task5()
    print '\nTask 6:', task6()
    print '\nTask 7:', task7()
    print '\nTask 8:', task8()
    print '\nTask 9:', task9()
    print '\nTask 10:', task10()

