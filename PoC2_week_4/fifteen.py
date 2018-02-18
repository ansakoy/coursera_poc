"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors

TEMPLATE: http://www.codeskulptor.org/#poc_fifteen_template.py
DESCRIPTION: https://www.coursera.org/learn/principles-of-computing-2/supplement/08FqM/mini-project-description
IMPLEMENTATION: http://www.codeskulptor.org/#user44_DfSBTRFXEe_0.py
OWLTEST: http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_fifteen_tests.py&urlPylintConfig=poc.pylint_config.py&imports=%7Bpoc:(poc_fifteen_gui)%7D
"""

# import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        target_pos = self.get_number(target_row, target_col)
        if target_pos != 0:
            return False
        if target_col == self._width - 1 and target_row == self._height - 1:
            return True
        max_val = self._width * self._height - 1
        previous_vals = list()
        for row in range(target_row, self._height):
            for col in range(self._width):
                previous_vals.append(self.get_number(row, col))
        relevant_vals = previous_vals[target_col + 1:]
        if relevant_vals[-1] != max_val:
            return False
        initial = relevant_vals[0] - 1
        for val in relevant_vals:
            difference = val - initial
            if difference != 1:
                return False
            initial = val
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # find target tile
        if target_col == self._width - 1 and target_row == self._height - 1:
            target_val = self._width * self._height - 1
        elif target_col == self._width - 1:
            prev_row = target_row + 1
            prev_col = 0
            prev_val = self.get_number(prev_row, prev_col)
            target_val = prev_val + 1
        else:
            prev_val = self.get_number(target_row, target_col + 1)
            target_val = prev_val + 1
        current_pos = (0, 0)
        for row in range(0, target_row + 1):
            for col in range(self._width + 1):
                value = self.get_number(row, col)
                if value == target_val:
                    current_pos = row, col
                    break

        current_row = current_pos[0]
        current_col = current_pos[1]

        moves = {'left_down': 'rddlu',
                 'from_corner_to_right': 'rdl',
                 'else_to_right': 'urrdl'}

        # scenario 1: same row
        if target_row == current_pos:
            move_to_current = 'l' * abs(target_col - current_col)
            self.update_puzzle(move_to_current)
            while not self.lower_row_invariant(target_row, target_col - 1):
                self.update_puzzle(moves['else_to_right'])

        # scenario 2: target value above and left
        elif current_col < target_col:
            move_to_current = 'l' * abs(target_col - current_col) + 'u' * abs(target_row - current_row)
            self.update_puzzle(move_to_current)
            current_row += 1
            if current_row == target_row and current_col == 0:
                self.update_puzzle(moves['from_corner_to_right'])
            else:
                while current_row != target_row:
                    self.update_puzzle(moves['left_down'])
                    current_row += 1
            while not self.lower_row_invariant(target_row, target_col - 1):
                self.update_puzzle(moves['else_to_right'])

        # scenario 3: target value straight above or to the right
        else:
            move_to_current = 'u' * abs(target_row - current_row) + 'r' * abs(target_col - current_col)
            self.update_puzzle(move_to_current)
            current_row += 1


        return ""

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))


