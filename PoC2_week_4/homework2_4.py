'''
FIFTEEN TEMPLATE: http://www.codeskulptor.org/#poc_fifteen_template.py
'''

def task1():
    '''
    A 4x4 puzzle in its solved configuration is shown below.
    Which configuration is the result of applying the move string "drdr" to the puzzle?
    '''
    return 'Easily checked by entering "drdr" into the template GUI'


def task2():
    '''
    Which move string updates the puzzle from the configuration
    shown on the left to the configuration shown on the right?
    Note that on the left, the tiles ten to fifteen are in their correct locations.
    On the right, tile nine has also been moved to its correct location.
    '''
    return 'Also easily checked by entering "drdr" into the template GUI'


def task3():
    '''
    For the next three problems, we will focus on exploring the behavior of a 2x2 puzzle.
    The size of the puzzle is passed to the initializer for the Puzzle class as a height and a width.
    Modify the last line of the template to create a 2x2 puzzle.
    Now, from the solved configuration, enter the move string "rdlu" repeatedly.
    How many times do you need to enter this string to return the puzzle to its solved configuration?
    '''
    return 3


def task4():
    '''
    Starting from the configuration shown below,
    which move string returns the 2x2 puzzle to its solved configuration?
    '''
    return 'Easily checked by entering "drdr" into the template GUI'


def task5():
    '''
    For configuration shown below,
    which of the following move strings return the puzzle to its solved configuration?
    '''
    return 'Easily checked by entering "drdr" into the template GUI'


def task6():
    '''
    Phase one will have one invariant lower_row_invariant(i, j)
    which is true prior to solving for the tile at position (i,j) (where i>1).
    This invariant consists of the following conditions:
    - Tile zero is positioned at (i,j).
    - All tiles in rows i+1 or below are positioned at their solved location.
    - All tiles in row i to the right of position (i,j) are positioned at their solved location.
    Problem: Which of the configurations below satisfy the invariant lower_row_invariant(2, 1)?
    '''
    return 'Simple enough, but may be variations in task and therefore solution'


def task7():
    '''
    Which annotated execution trace captures the relationship between the solution method
    solve_col0_tile and the invariant lower_row_invariant?
    Remember that once the entire ith row is solved, the solution process then proceeds
    to the rightmost column of the i-1st row.
    You may assume that the puzzle is m x n.
    (a)
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_col0_tile(i)
    assert my_puzzle.lower_row_invariant(i - 1, n)
    ...
    (b)
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_interior_tile(i, 0)
    assert my_puzzle.lower_row_invariant(i - 1, n - 1)
    ...
    (c)
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_col0_tile(i)
    assert my_puzzle.lower_row_invariant(i, n - 1)
    ...
    (d)
    ...
    assert my_puzzle.lower_row_invariant(i, 0)
    my_puzzle.solve_col0_tile(i)
    assert my_puzzle.lower_row_invariant(i - 1, n -1)
    ...
    '''
    return '(d)'


def task8():
    '''
    Problem: Starting from the configuration on the right,
    which move string completes the solution process for this position
    and updates the puzzle to a configuration where lower_row_invariant(3, 0) is true?
    '''
    return 'lddruld'


def task9():
    '''
    Problem: Which move string below updates the puzzle from the left configuration
    into the right configuration above?
    '''
    return "ruldrdlurdluurddlur"


def task10():
    '''
    Problem: Which move string below updates the left configuration into the right configuration?
    '''
    return "urdlurrdluldrruld"

if __name__ == '__main__':
    pass