'''
SOURCES:
RECURRENCE PLOT: http://www.codeskulptor.org/#poc_recurrence_plot.py
'''

import math

import poc_cat_in_the_hat

COUNT = 0


def task1():
    '''
    Examine the behavior of this recursive program
    http://www.codeskulptor.org/#poc_cat_in_the_hat.py
    that models the story of the "Cat in the Hat" by Dr. Suess.
    How many calls to the function clean_up are made by the program?
    '''
    poc_cat_in_the_hat.clean_up("Cat in the Hat", 0)


def task2():
    '''
    Consider the following Python function
        def add_up(n):
            if n == 0:
                return 0
            else:
                return n + add_up(n - 1)
    If n is non-negative integer, enter a math expression in n for the value returned by add_up(n)
    '''
    def recursive_add_up(n):
        if n == 0:
            return 0
        else:
            return n + recursive_add_up(n - 1)
    # print 'By recursion:', recursive_add_up(60)

    def math_add_up(n):
        return (n * (n + 1)) / 2
    # print 'By formula:', math_add_up(60)
    return '(n * (n + 1)) / 2'


def task3():
    '''
    Consider the following Python function
    def multiply_up(n):
        if n == 0:
            return 1
        else:
            return n * multiply_up(n - 1)
    If n is non-negative integer, enter a math expression in n for the value returned by multiply_up(n)
    '''

    def recursive_multiply_up(n):
        if n == 0:
            return 1
        else:
            return n * recursive_multiply_up(n - 1)
    # print recursive_multiply_up(2)
    # print recursive_multiply_up(3)
    # print recursive_multiply_up(4)
    # print recursive_multiply_up(5)

    def math_multiply_up(n):
        return math.factorial(n)
    # print math_multiply_up(2)
    # print math_multiply_up(3)
    # print math_multiply_up(4)
    # print math_multiply_up(5)

    return 'n!'


def task4():
    '''
    Consider this recursive Python function that computes the Fibonacci numbers below:
    http://en.wikipedia.org/wiki/Fibonacci_number
    def fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num - 2)
    Let f(n) be the total number of calls to the function fib
    that are computed during the recursive evaluation of fib(n).
    Which recurrence reflects the number of times that fib is called
    during this evaluation of fib(n)?

    You may want to add a global counter to the body of fib
    that records the number of calls for small values of n.
    '''

    def fib(num):
        global COUNT
        COUNT += 1
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num - 2)
    # index = 0
    # index = 1
    # index = 2
    # index = 3
    # index = 4
    # index = 5
    # index = 7
    # index = 6
    # print fib(index)
    # print 'Function fib({}) was executed {} times'.format(index, COUNT)
    return "f(0)=1\n" \
           "f(1)=1\n" \
           "f(n)=2*f(n-1)+1"


def task5():
    '''
    The number of recursive calls to fib in the previous problem grows quite quickly.
    The issue is that fib fails to "remember" the values computed during previous recursive calls.
    One technique for avoiding this issue is memoization,
    a technique in which the values computed by calls to fib are stored
    in an auxiliary dictionary for later use.
    The Python function below uses memoization to compute the Fibonacci numbers efficiently.
    def memoized_fib(num, memo_dict):
        if num in memo_dict:
            return memo_dict[num]
        else:
            sum1 = memoized_fib(num - 1, memo_dict)
            sum2 = memoized_fib(num - 2, memo_dict)
            memo_dict[num] = sum1 + sum2
            return sum1 + sum2
    If n>0, how many calls to memoized_fib are computed during the evaluation
    of the expression memoized_fib(n, {0 : 0, 1 : 1})? Enter the answer as a math expression in n below.
    You may want to add a global counter to the body of memoized_fib keeps track of the number of calls.
    '''

    def memoized_fib(num, memo_dict):
        global COUNT
        COUNT += 1
        print memo_dict
        if num in memo_dict:
            return memo_dict[num]
        else:
            sum1 = memoized_fib(num - 1, memo_dict)
            sum2 = memoized_fib(num - 2, memo_dict)
            memo_dict[num] = sum1 + sum2
            return sum1 + sum2
    # index = 0
    # index = 1
    # index = 2
    # index = 3
    # index = 4
    index = 5
    # index = 6
    # index = 7
    memoized_fib(index, {0: 0, 1: 1})
    # print 'Function memoized_fib({}, dict(0: 0, 1: 1)) was executed {} times'.format(index, COUNT)
    return '2*n - 1'


def task6():
    '''
    Given a list outcomes of length n, we can perform the following recursive computation
    to generate the set of all permutations of length n:

    - Compute the set of permutations rest_permutations for the list outcomes[1 :] of length n - 1,
    - For each permutation perm in rest_permutations, insert outcome[0]
    at each possible position of perm to create permutations of length n,
    - Collect all of these permutations of length n into a set and return that set.

    If p(n) is the number of permutations returned by this method,
    what recurrence below captures the behavior of p(n)?
    '''
    def gen_permutations(outcomes):
        # base case
        if len(outcomes) == 0:
            return [[]]
        # recursion case
        result = list()
        first = outcomes[0]
        rest = outcomes[1:]
        print first, rest
        rest_permutations = gen_permutations(rest)
        for perm in rest_permutations:
            for idx in xrange(len(perm) + 1):
                target = perm[:]
                target.insert(idx, first)
                result.append(target)
        return result

    outc = ['a', 'b', 'c', 'd']
    print gen_permutations(outc)
    return 'p(0) = 1\np(n) = n * p(n - 1)'


def task7():
    '''
    Using the math notes for recurrences, look up the solution to the recurrence from problem #6.
    https://www.coursera.org/learn/principles-of-computing-2/supplement/1YrGZ/math-notes-on-recurrence-relation?utm_medium=email&utm_source=other&utm_campaign=notifications.auto.8U5YJwwCEea8UxJET5iscw
    f(n)=f(n-1)+1 -> f(n)=n
    f(n)=f(n-1)+n -> f(n)=12n(n+1)
    f(n)=2f(n-1) -> f(n)=2n-1
    f(n)=n f(n-1) -> f(n)=n!
    f(n)=f(n2)+1 -> f(n)~log2(n)+1
    f(n)=f(n2)+n -> f(n)~2n-1
    f(n)=2f(n2) -> f(n)~n
    f(n)=2f(n2)+1 -> f(n)~2n-1
    f(n)=2f(n2)+n -> f(n)~n(log2(n)+1)
    Enter the solution to this recurrence (as given in the notes) as a math expression in n below.
    '''
    return 'n!'


def task8():
    '''
    As part of this week's mini-project, you will implement a function merge(list1, list2)
    that takes two ordered lists and merges the lists into a single ordered list
    that contains all of the elements in either list1 and list2.

    The body of merge consists of a while loop that iterates until one of the lists list1 and list2 is empty.
    Each iteration of the loop compares the first element in each list,
    pops the smaller element from its containing list and appends this element to the answer.
    Once one list is exhausted, the entries in the remaining list are appended to the answer.

    If list1 and list2 are both of length n,
    which expression below grows at the same rate as the running time
    (i.e; the number of Python statements executed) of merge?
    '''
    return  'n'


def task9():
    '''

    :return:
    '''



if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    task6()
