# TEMPLATE: http://www.codeskulptor.org/#poc_zombie_template.py
# OWLTEST: http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_zombie_tests.py&urlPylintConfig=poc.pylint_config.py&imports=%7Bpoc:(poc_grid,poc_queue,poc_zombie_gui)%7D&
# IMPLEMENTATION: http://www.codeskulptor.org/#user43_fPx00lrnzf_5.py


import random
import poc_grid
import poc_queue
# import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        self._zombie_list = list()
        self._human_list = list()
        if zombie_list:
            self._zombie_list = zombie_list
        if human_list:
            self._human_list = human_list

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = list()
        self._zombie_list = list()
        poc_grid.Grid.clear(self)

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        height = self.get_grid_height()
        width = self.get_grid_width()
        if entity_type == HUMAN:
            cells = self._human_list
        else:
            cells = self._zombie_list
        visited = poc_grid.Grid(height, width)
        distance_field = [[height * width for dummy_col in xrange(width)]
                          for dummy_row in xrange(height)]
        boundary = poc_queue.Queue()
        for cell in cells:
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0
            boundary.enqueue(cell)
        while len(boundary):
            current_cell = boundary.dequeue()
            # if entity_type == HUMAN:
            #     neighbors = visited.eight_neighbors(current_cell[0], current_cell[1])
            if entity_type == HUMAN:
                neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            else:
                neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
                    visited.set_full(neighbor[0], neighbor[1])
        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_humans = list()
        for human in self.humans():
            directions = self.eight_neighbors(human[0], human[1])
            best_distance = 0
            best_destination = human
            for coord in directions:
                if self.is_empty(coord[0], coord[1]):
                    distance = zombie_distance_field[coord[0]][coord[1]]
                    if distance > best_distance:
                        best_distance = distance
                        best_destination = coord[0], coord[1]
            new_humans.append(best_destination)
        self._human_list = new_humans

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombies = list()
        for zombie in self.zombies():
            directions = self.four_neighbors(zombie[0], zombie[1])
            best_distance = human_distance_field[zombie[0]][zombie[1]]
            best_destination = zombie
            for coord in directions:
                if self.is_empty(coord[0], coord[1]):
                    distance = human_distance_field[coord[0]][coord[1]]
                    if distance < best_distance:
                        best_distance = distance
                        best_destination = coord[0], coord[1]
            new_zombies.append(best_destination)
        self._zombie_list = new_zombies

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))


if __name__ == '__main__':
    # apocalypse = Apocalypse(4, 6, zombie_list=[(1, 5), (3, 2)], human_list=[(3, 2), (0, 1)])
    # z_dist = apocalypse.compute_distance_field(ZOMBIE)
    # print [h for h in apocalypse.humans()]
    # print z_dist
    # apocalypse.move_humans(z_dist)

    # h_dist = apocalypse.compute_distance_field(HUMAN)
    # print [z for z in apocalypse.zombies()]
    # print h_dist
    # apocalypse.move_zombies(h_dist)
    # obj = Apocalypse(3, 3, [], [], [(2, 2)])
    # df = obj.compute_distance_field(HUMAN)
    # for r in df:
    #     print r
    obj = Apocalypse(3, 3, [], [(1, 1)], [(1, 1)])
    dist = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
    obj.move_zombies(dist)
    for z in obj.zombies():
        print z
