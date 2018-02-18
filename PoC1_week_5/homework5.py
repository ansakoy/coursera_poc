def task1():
    '''
    Use the function run_simulations in the greedy boss simulator
    to plot the graph of total salary earned as a function of the number of days
    for bribe_cost_increment = 0, 500, 1000, 2000.
    Which value for bribe_cost_increment generates the fastest growth
    in total salary earned in the simulation?
    Remember to compare the plots of the functions over roughly the same number of days.
    '''
    return 0


def task2():
    '''
    One scenario that the greedy boss simulator does not cover
    is the situation when you refuse to accept a bribe.
    Which of the following arithmetic sums evaluates to your total salary earned after d days?
    '''
    return "100 + 100 + ... + 100 + 100 (with d terms in sum)"


def task3():
    '''
    Reduce the arithmetic sum that you selected in Question 2 to a polynomial expression
    in the number of days d using the rules for arithmetic sums specified in the Math notes.
    This expression should evaluate to your total salary earned after d days.
    '''
    return '100 * d'


def task4():
    '''
    For the next three problems, we will consider the case when bribe_cost_increment == 1000.
    First, convert the output of greedy_boss() into Log/Log form by taking the logarithm
    of both current_day and the total salary earned using math.log()
    before they appended to the list days_vs_earnings.

    The plot of the resulting graph approaches a straight line as the number of days increase.
    This observation signals that the function might be a polynomial function.
    Compute the slope of this line and round it to the nearest integer to estimate the degree of this polynomial.
    '''
    #???????????????????
    return 200


def task5():
    '''
    Examine the output of the simulation greedy_boss(50, 1000).
    Note you accumulate enough savings to pay a bribe once every 10 days.

    Which of the arithmetic sums below evaluates to the total salary earned after n bribes?
    '''
    return "1000 + 2000 + 3000 +...+ 1000n"


def task6():
    '''
    Reduce the arithmetic sum that you selected in Question 5 to a closed-form expression in n
    using the rules for arithmetic sums specified in the Math notes.
    This expression should relate total salary earned to the number of bribes.
    Finally, use the fact that each bribe happens once every 10 days to derive a polynomial expression
    that approximates the total salary earned in terms of the number of days d.
    As a check, this expression in d should evaluate exactly to the total salary
    earned by the end of the day of each bribe.
    Enter this expression in d as a math expression below.
    '''
    return '(1/2)*(d+1)*d*1000'


def task7():
    '''
    The next two questions will examine the case when the cost of a bribe does not increase,
    i.e; bribe_cost_increment == 0.
    Our first task is to check whether the total salary earned is a polynomial function of the number of days in this case.
    To this end, create a Log/Log plot of the output of greedy_boss and examine the resulting graph.
    Does the graph approach a straight line as the number of days increases?
    '''
    return 'No, the graph does not approach a straight line.'


def task8():
    '''
    To conclude our analysis of this case, we will do some manual experimentation
    to locate an expression in d that grows at a similar rate to total salary earned
    when bribe_cost_increment == 0.

    Compare the growth rates of the expressions below to the growth rate of total salary earned
    using the plotting technique described in the Math notes.
    Which expression grows at approximately the same rate as total salary earned?
    '''
    # COMPARISON http://www.codeskulptor.org/#user43_LDuQuMcZ7q_1.py
    return '95 * d ** 2'


def task9():
    '''
    In the next two questions, we will consider a simple version of Cookie Clicker
    in which there is only one possible upgrade option.
    Instead of increasing the cost of an upgrade by some fixed amount after each upgrade
    as done in the greedy boss simulator,
    each upgrade in Cookie Clicker costs 15% more than the cost of the previous upgrade.
    (Note that this cost compounds in the same manner that interest does.)
    If the first upgrade costs one unit, enter a math expression that models
    the cost of the nth upgrade.
    '''
    return '1.15^(n-1)'


def task10():
    '''
    For the case when bribe_cost_increment == 1000, the cost of the nth bribe was exactly 1000n.
    Which expression in n grows faster (as defined in the Math notes),
    1000n or your answer to question 9?
    You may want to plot some examples using SimplePlot for large values of n to help in making this comparison.
    '''
    return 'The cost of an upgrade in Cookie Clicker grows faster than the cost of a bribe in the greedy boss scenario.'


def task11():
    '''
    To complete this problem, visit this OwlTest page
    http://codeskulptor.appspot.com/owltest/?urlTests=poc.poc_merge_tests_final.py&urlPylintConfig=skip
    and follow the directions for creating and submitting a list of test cases.
    OwlTest will run the submitted test cases against a suite of erroneous implementations
    of merge() and compare results versus those computed by our reference implementation.
    This program
    http://www.codeskulptor.org/#poc_merge_testing.py
    is an example of how you should construct your test case file.
    It includes two test cases which will be the inputs to the merge function: [2] and [2, 0].
    my_tests: http://www.codeskulptor.org/#user43_rDUvJ63xI2_1.py
    '''
    TEST_CASES = [[2], [2, 0], [0, 0, 0, 0, 0], [4, 8, 4, 4, 8],
                  [4, 8, 4, 8, 8], [4, 8, 4, 4, 4, 4],
                  [8, 2, 2, 8, 4, 4, 4], [0, 0, 0, 2, 0]]
    return TEST_CASES




