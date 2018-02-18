"""
SOURCE: http://www.codeskulptor.org/#poc_tantrix_template.py
DESCRIPTION: https://www.coursera.org/learn/principles-of-computing-2/supplement/l57zN/practice-activity-solitaire-tantrix
IMPLMENTATION: http://www.codeskulptor.org/#user43_fn3wVK46mm_3.py
SOLUTION: http://www.codeskulptor.org/#poc_tantrix_solution.py

Student facing code for Tantrix Solitaire
http://www.jaapsch.net/puzzles/tantrix.htm

Game is played on a grid of hexagonal tiles.
All ten tiles for Tantrix Solitaire and place in a corner of the grid.
Click on a tile to rotate it.  Cick and drag to move a tile.

Goal is to position the 10 provided tiles to form
a yellow, red or  blue loop of length 10
"""

# Core modeling idea - a triangular grid of hexagonal tiles are
# model by integer tuples of the form (i, j, k)
# where i + j + k == size and i, j, k >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree intervals
DIRECTIONS = {0: (-1, 0, 1), 1: (-1, 1, 0), 2: (0, 1, -1),
              3: (1, 0, -1), 4: (1, -1, 0), 5: (0, -1, 1)}


def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions


# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                   "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]

# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4


class Tantrix:
    """
    Basic Tantrix game class
    """

    def __init__(self, size):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        """
        assert size >= MINIMAL_GRID_SIZE
        self._grid_size = size
        # Initialize dictionary tile_value to contain codes for ten
        self._tile_value = dict()
        hexagon_grid = list()
        for first in xrange(size + 1):
            for second in xrange(size + 1):
                third = size - (first + second)
                if third >= 0:
                    hexagon_grid.append((first, second, third))
        # print hexagon_grid
        for index in xrange(len(SOLITAIRE_CODES)):
            self._tile_value[hexagon_grid[index]] = SOLITAIRE_CODES[index]
        # tiles in Solitaire Tantrix in one 4x4 corner of grid
        pass

    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        printed_output = ''
        for tile in self._tile_value:
            printed_output += str(tile) + ': ' + self._tile_value[tile] + '\n'
        return printed_output

    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self._grid_size

    def tile_exists(self, index):
        """
        Return whether a tile with given index exists
        """
        if self._tile_value.get(index):
            return True
        return False

    def place_tile(self, index, code):
        """
        Place a tile with code at cell with given index
        """
        self._tile_value[index] = code

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index
        and return the code value for that tile        """
        return self._tile_value.pop(index)

    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        """
        tile = self._tile_value[index]
        rotated_tile = tile[-1] + tile[0: -1]
        # self._tile_value[index] = rotated_tile
        self.place_tile(index, rotated_tile)

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        """
        return self._tile_value[index]

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in given direction
        """
        difference = DIRECTIONS[direction]
        neighbor = [difference[idx] + index[idx] for idx in xrange(len(index))]
        return tuple(neighbor)

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for adjacent tiles
        """
        all_tiles = self._tile_value.keys()
        corresponding_positions = dict()
        for direction in DIRECTIONS.keys():
            if direction < 3:
                corresponding_positions[direction] = direction + 3
            else:
                corresponding_positions[direction] = direction - 3
        # print corresponding_positions
        for tile_index in all_tiles:
            for direction in DIRECTIONS:
                neighbor = self.get_neighbor(tile_index, direction)
                if self.tile_exists(neighbor):
                    current_color = self._tile_value[tile_index][direction]
                    neighbor_color = self._tile_value[neighbor][corresponding_positions[direction]]
                    # print current_color, neighbor_color
                    if current_color != neighbor_color:
                        return False
        return True

    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """
        # if not self.is_legal():
        #     return False
        starting_positions = self._tile_value.keys()[0]
        starting_tile = self._tile_value[starting_positions]
        current_length = 1
        target_length = len(SOLITAIRE_CODES)
        print starting_positions
        direction = starting_tile.index(color)
        next_tile_index = self.get_neighbor(starting_positions, direction)
        next_tile = self._tile_value.get(next_tile_index)
        if not next_tile:
            return False
        corresponding_index = reverse_direction(direction)
        next_direction = next_tile.index(color)
        if next_direction == corresponding_index:
            for idx in xrange(len(next_tile)):
                if next_tile[idx] == color and idx != corresponding_index:
                    next_direction = idx
                    break
        while True:
            current_length += 1
            if next_tile_index == starting_positions and current_length >= target_length:
                return True
            elif next_tile_index == starting_positions and current_length < target_length:
                return False
            next_tile_index = self.get_neighbor(next_tile_index, next_direction)
            next_tile = self._tile_value.get(next_tile_index)
            if not next_tile:
                return False
            direction = next_direction
            corresponding_index = reverse_direction(direction)
            next_direction = next_tile.index(color)
            if next_direction == corresponding_index:
                for idx in xrange(len(next_tile)):
                    if next_tile[idx] == color and idx != corresponding_index:
                        next_direction = idx
                        break




# run GUI for Tantrix
# import poc_tantrix_gui
#
# poc_tantrix_gui.TantrixGUI(Tantrix(6))

if __name__ == '__main__':
    tantr = Tantrix(4)
    print tantr
    # print tantr.get_neighbor((0, 3, 1), 3)
    # tantr.is_legal()
    tantr.has_loop('Y')