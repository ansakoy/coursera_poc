"""
Merge function for 2048 game.
"""
# http://www.codeskulptor.org/#user42_6kUJz4y3wp_0.py


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = list()
    working_list = [num for num in line if num != 0]
    next_step = 0
    while next_step < len(working_list):
        first = working_list[next_step]
        try:
            second = working_list[next_step + 1]
            if first == second:
                new_line.append(first + second)
                next_step += 2
            else:
                new_line.append(first)
                next_step += 1
        except IndexError:
            new_line.append(first)
            break
    new_line.extend([0 for dummy_pos in line[len(new_line):]])
    return new_line


def test_merge():
    print 'input [4, 8, 4, 4, 8], computed:', merge([4, 8, 4, 4, 8]), 'expected: [4, 8, 8, 8, 0]'
    print 'input [4, 8, 4, 8, 8], computed:', merge([4, 8, 4, 8, 8]), 'expected: [4, 8, 4, 16, 0]'
    print 'input [4, 8, 4, 4], computed:', merge([4, 8, 4, 4]), 'expected: [4, 8, 8, 0]'
    print 'input [4, 8, 4, 4, 4, 4], computed:', merge([4, 8, 4, 4, 4, 4]), 'expected: [4, 8, 8, 8, 0, 0]'
    print 'input [8, 2, 2, 8, 4, 4, 4], computed:', merge([8, 2, 2, 8, 4, 4, 4]), 'expected: [8, 4, 8, 8, 4, 0, 0] '
    print 'input [0, 0, 0, 0, 0], computed:', merge([0, 0, 0, 0, 0]), 'expected: [0, 0, 0, 0, 0]'
    print 'input [0, 0, 0, 2, 0], computed:', merge([0, 0, 0, 2, 0]), 'expected: [2, 0, 0, 0, 0]'


if __name__ == '__main__':
    test_merge()