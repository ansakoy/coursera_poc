def task1():
    '''
    Review the math notes on the growth of functions.
    https://www.coursera.org/learn/principles-of-computing-2/supplement/OTIAb/math-notes-on-growth-rates-of-functions
    Which of the following functions grow at the same rate as
    (1/2.0) * n ** 2 - 5 * n + 20
    http://www.codeskulptor.org/#poc_growth_plot.py
    '''
    # http://www.codeskulptor.org/#user43_60mF5fT0Np_1.py
    return 'n ** 2'

def task2():
    '''
    The fastest algorithms for sorting a list of size n share a bound
    (specified as a simple expression in n)
    for the minimal number of comparisons required to sort any list of length n.

    Use a web search engine (like Google)
    to look up this estimate and select the answer below
    that grows at the same rate as this expression.
    '''
    return 'n * math.log(n)'


def task3():
    '''
    Review this week's practice activity on sorting strings.
    https://www.coursera.org/learn/principles-of-computing-2/supplement/CG4Vb/practice-activity-sorting-strings
    http://www.codeskulptor.org/#poc_string_sort.py
    The activity discusses a grid-based method for sorting strings
    that does not require comparisons.
    Given a list of n three-letter words, which expression
    grows as the same rate as the number of statements executed during this sort?
    '''
    return 'n'


def task4():
    '''
    Consider a stack in which we have performed n pushes followed by n pops.
    Which of the following are true statements concerning this sequence of operations?
    '''
    options = {'The first element pushed onto the stack is the last element popped off of the stack.': True,
               'The first element pushed onto the stack is the first element popped off of the stack.': False,
               'The last element pushed onto the stack is the last element popped off of the stack.': False,
               'The last element pushed onto the stack is the first element popped off of the stack.': True}
    answer = list()
    for option in options:
        if options[option]:
            answer.append(option)
    return answer


def task5():
    '''
    Consider a queue in which we have performed n enqueues followed by n dequeues.
    Which of the following are true statements concerning this sequence of operations?
    '''
    options = {'The first element enqueued into the queue is the last element dequeued out of the queue.': False,
               'The last element enqueued into the queue is the first element dequeued out of the queue.': False,
               'The last element enqueued into the queue is the last element dequeued out of the queue.': True,
               'The first element enqueued into the queue is the first element dequeued out of the queue.': True}
    answer = list()
    for option in options:
        if options[option]:
            answer.append(option)
    return answer


def task6():
    '''
    Review the provided implementation for this week's grid class.
    http://www.codeskulptor.org/#poc_grid.py
    In this implementation, the methods four_neighbors and eight_neighbors
    treat the boundaries of the grid as being impassable.

    An alternative approach is to treat cells with the same row index
    on the left and right boundaries as being adjacent and cells with the same column index
    on the top and bottom boundaries as being adjacent.
    '''
    from poc_grid import Grid
    grid = Grid(3, 2)
    result = grid.four_neighbors_circle(0, 1)
    return 'up = (row - 1) % self._grid_height\n' \
           'down = (row + 1) % self._grid_height\n' \
           'left = (col - 1) % self._grid_width\n' \
           'right = (col + 1) % self._grid_width\n' \
           'return [[up, col], [down, col], [row, left], [row, right]]'


def task7():
    '''
    Consider the wildfire demo from lecture,
    http://www.codeskulptor.org/#poc_wildfire_student.py
    which line in the implementation of update_boundary checks whether the fire can spread to an unburned cell?
    '''
    return 'if self.is_empty(neighbor[0], neighbor[1]): - ???'


def task8():
    '''
    Consider the case in which one steps through the entire
    breadth first search of the grid in the wildfire demonstration.
    Which of the following expressions grows at the same rate
    as the number of statements executed during this breadth first search?
    Assume the grid has size m-by-n.
    '''
    return 'n * m - ???'


def task9():
    '''
    Complete this template and implement a Stack class.
    http://www.codeskulptor.org/#poc_stack_template.py
    Once your implementation is complete,
    uncomment the test code at the end of the template
    and enter the number printed out by this template.
    '''
    from poc_stack import home_work_test
    result = home_work_test()
    return result


def task10():
    '''
    Take the provided Queue class available here
    http://www.codeskulptor.org/#poc_queue.py
    and modify the enqueue and dequeue methods to behave like the push and pop methods
    for your Stack class.
    Save this modified class definition.
    Then, take the wildfire demo
    http://www.codeskulptor.org/#poc_wildfire_student.py
    and import this modified definition for the Queue class at the top of the wildfire demo code.
    In CodeSkulptor, the modified import statement would have the form:
    import userXX_XXXXX as poc_queue
    Now, run this modified demo and add a single cell in the middle of the canvas
    to the boundary queue prior to starting the search.
    Which of the images below correspond to a possible state of the grid
    during the resulting depth first search?
    '''

    modified_queue = 'http://www.codeskulptor.org/#user43_3bBY25cOjI_1.py'
    modified_wildfire = 'http://www.codeskulptor.org/#user43_T0PxAUZuQM_1.py'
    return modified_wildfire


# if __name__ == '__main__':
#     print task9()