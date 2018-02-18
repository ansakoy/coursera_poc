# TEMPLATE: http://www.codeskulptor.org/#poc_clicker_template.py
# BUILDINFO: http://www.codeskulptor.org/#poc_clicker_provided.py
# IMPLEMENTATION: http://www.codeskulptor.org/#user43_In5XOsuk4OUup8c.py

"""
Cookie Clicker Simulator
"""
try:
    import simpleplot

    # Used to increase the timeout, if necessary
    import codeskulptor
except ImportError:
    pass

# codeskulptor.set_timeout(20)
import random
import math

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_num_cookies = 0.0  # Total number of cookies produced throughout the game (initialized to 0.0)
        self._current_num_cookies = 0.0  # Current number of cookies you have (initialized to 0.0)
        self._current_time = 0.0  # Current time (in seconds) of the game (initialized to 0.0)
        self._current_cps = 1.0  # The current CPS (this should be initialized to 1.0)
        self._history = [(0.0, None, 0.0, 0.0)]  # History: list of tuples. Each: time, item, cost, total num of cookies

    def __str__(self):
        """
        Return human readable state
        """
        return "Time: %s\n" \
               "Current Cookies: %s\n" \
               "CPS: %s\n" \
               "Total Cookies: %s" %(self._current_time,
                                          self._current_num_cookies,
                                          self._current_cps,
                                          self._total_num_cookies)

    def get_cookies(self):
        """
        Return current number of cookies (not total number of cookies)
        Should return a float
        """
        return self._current_num_cookies

    def get_total_cookies(self):
        """
        Return total number of cookies
        Should return a float
        """
        return self._total_num_cookies


    def get_cps(self):
        """
        Get current CPS
        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time
        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list
        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)
        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history[:]

    def print_history(self):
        '''
        nicely prints the history of the game
        '''
        print 'Time\tItem\tCost\tTotal_cookies'
        for episode in self._history:
            print episode[0], '\t', episode[1], '\t', episode[2], '\t', episode[3]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies <= self._current_num_cookies:
            return 0.0
        difference = cookies - self._current_num_cookies
        return math.ceil(difference / self._current_cps)

    def wait(self, time):
        """
        Wait for given amount of time and update state
        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._current_num_cookies += self._current_cps * time
            self._total_num_cookies += self._current_cps * time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        Should do nothing if you cannot afford the item
        """
        if self._current_num_cookies >= cost:
            self._current_num_cookies -= cost
            self._current_cps += additional_cps
            episode = (self._current_time, item_name, cost, self._total_num_cookies)
            self._history.append(episode)


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    clicker = ClickerState()
    build_clone = build_info.clone()
    while True:
        time_left = duration - clicker.get_time()
        if time_left < 0:
            break
        next_item = strategy(clicker.get_cookies(), clicker.get_cps(),
                             clicker.get_history(), time_left, build_clone)
        if not next_item:
            break
        cost = build_clone.get_cost(next_item)
        time_needed = clicker.time_until(cost)
        if time_needed > time_left:
            break
        clicker.wait(time_needed)
        clicker.buy_item(next_item, cost, build_clone.get_cps(next_item))
        build_clone.update_item(next_item)
    remainder = duration - clicker.get_time()
    if remainder:
        clicker.wait(remainder)
    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cheapest = float('inf')
    next_item = None
    for item in build_info.build_items():
        cost = build_info.get_cost(item)
        cookies_needed = cost - cookies
        time_needed = cookies_needed / cps
        if time_needed <= time_left and cost < cheapest:
            cheapest = cost
            next_item = item
    return next_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    most_expensive = - float('inf')
    next_item = None
    for item in build_info.build_items():
        cost = build_info.get_cost(item)
        cookies_needed = cost - cookies
        time_needed = cookies_needed / cps
        if time_needed <= time_left and cost > most_expensive:
            most_expensive = cost
            next_item = item
    # print next_item, most_expensive
    return next_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    next_item = None
    best_ratio = - float('inf')
    for item in build_info.build_items():
        cost = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        ratio = item_cps / cost
        cookies_needed = cost - cookies
        time_needed = cookies_needed / cps
        if time_needed <= time_left and ratio > best_ratio:
            best_ratio = ratio
            next_item = item
    return next_item


def strategy_absolute_random(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    items = build_info.build_items()
    next_item = items[random.randrange(len(items))]
    return next_item


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state
    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Absolute Random", SIM_TIME, strategy_absolute_random)
    run_strategy("Best", SIM_TIME, strategy_best)
    # run_strategy("None", SIM_TIME, strategy_none)


run()