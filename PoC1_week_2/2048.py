# OWL TEST: http://codeskulptor.appspot.com/owltest/?urlTests=poc.poc_2048_tests.py&urlPylintConfig=poc.pylint_config.py&imports=%7Bpoc:(poc_2048_gui)%7D
# TEMPLATE: http://www.codeskulptor.org/#poc_2048_template.py
# RESULT: http://www.codeskulptor.org/#user43_eOHW80qRzK_7.py

"""
Clone of 2048 game.
"""

import random

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
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


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = list()
        self._initial_tiles = {UP: [(0, var) for var in range(self._grid_width)],
                              DOWN: [(self._grid_height - 1, var) for var in range(self._grid_width)],
                              LEFT: [(var, 0) for var in range(self._grid_height)],
                              RIGHT: [(var, self._grid_width - 1) for var in range(self._grid_height)]}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in xrange(self._grid_width)] for dummy_row in xrange(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid = ''
        str_rows = [str(row) + '\n' for row in self._grid]
        for row in str_rows:
            grid += row
        return grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_tiles = self._initial_tiles[direction]
        target_direction = OFFSETS[direction]
        if len(initial_tiles) == self._grid_height:
            num_steps = self._grid_width
        else:
            num_steps = self._grid_height
        change = False
        for tile in initial_tiles:
            values = list()
            path = list()
            for step in xrange(num_steps):
                row = tile[0] + step * target_direction[0]
                col = tile[1] + step * target_direction[1]
                values.append(self._grid[row][col])
                path.append((row, col))
            new_line = merge(values)
            for idx in xrange(len(new_line)):
                cell = path[idx]
                self._grid[cell[0]][cell[1]] = new_line[idx]
                if new_line[idx] != values[idx]:
                    change = True
        if change:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        values = [2 for dummy_pos in range(9)] + [4]
        current_grid = self.__str__()
        if '0' in current_grid:
            while True:
                random_height = random.choice(range(self._grid_height))
                random_width = random.choice(range(self._grid_width))
                if self._grid[random_height][random_width] == 0:
                    self._grid[random_height][random_width] = random.choice(values)
                    break
                else:
                    continue

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


# if __name__ == '__main__':
#     obj = TwentyFortyEight(4, 4)
#     print obj.reset()
#     obj.set_tile(0, 0, 2)
#     obj.set_tile(0, 1, 4)
#     obj.set_tile(0, 2, 8)
#     obj.set_tile(0, 3, 16)
#     obj.set_tile(1, 0, 16)
#     obj.set_tile(1, 1, 8)
#     obj.set_tile(1, 2, 4)
#     obj.set_tile(1, 3, 2)
#     obj.set_tile(2, 0, 0)
#     obj.set_tile(2, 1, 0)
#     obj.set_tile(2, 2, 8)
#     obj.set_tile(2, 3, 16)
#     obj.set_tile(3, 0, 0)
#     obj.set_tile(3, 1, 0)
#     obj.set_tile(3, 2, 4)
#     obj.set_tile(3, 3, 2)
#     obj.move(UP)
#     print obj.__str__()