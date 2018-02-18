import cookie_clicker



def test_get_history():
    state = cookie_clicker.ClickerState()
    copy_history = state.get_history()
    print 'before\n', copy_history
    copy_history[0] = 'UPD'
    print 'after\n', copy_history
    state.print_history()


def test_time_until():
    test_cases = {0.0: 0.0, 1.0: 1.0, 5.0: 5.0, 23.0: 23.0}
    state = cookie_clicker.ClickerState()
    for case in test_cases:
        expected = test_cases[case]
        actual = state.time_until(case)
        print 'Expected: {}, Result: {}'.format(expected, actual)
        if expected != actual:
            print '-------------------- DIFFERENT'


def test_wait():
    test_cases = {0.0: "Total cookies: 0.0\nCurrent cookies: 0.0\nCurrent time: 0.0\nCurrent CPS: 1.0",
                  1.0: "Total cookies: 1.0\nCurrent cookies: 1.0\nCurrent time: 1.0\nCurrent CPS: 1.0",
                  5.0: "Total cookies: 5.0\nCurrent cookies: 5.0\nCurrent time: 5.0\nCurrent CPS: 1.0",
                  23.0: "Total cookies: 23.0\nCurrent cookies: 23.0\nCurrent time: 23.0\nCurrent CPS: 1.0"}
    state = cookie_clicker.ClickerState()
    for case in test_cases:
        print '##### CASE: {} #####'.format(case)
        print state
        time_left = state.time_until(case)
        state.wait(time_left)
        print 'AFTER WAIT:'
        print 'EXPECTED:'
        print test_cases[case]
        print 'ACTUAL:'
        print state




if __name__ == '__main__':
    # test_get_history()
    # test_time_until()
    test_wait()
    state = cookie_clicker.simulate_clicker(cookie_clicker.provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), 5000.0, strategy_none)
    print state
    state = cookie_clicker.simulate_clicker(cookie_clicker.provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001],
                                                 'Grandma': [100.0, 0.5]}, 1.15), 400.0, cookie_clicker.strategy_cheap)
    print state
    state.print_history()

    state = cookie_clicker.simulate_clicker(cookie_clicker.provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001],
                                                 'Portal': [1666666.0, 6666.0], 'Shipment': [40000.0, 100.0],
                                                 'Grandma': [100.0, 0.5], 'Farm': [500.0, 4.0],
                                                 'Time Machine': [123456789.0, 98765.0],
                                                 'Alchemy Lab': [200000.0, 400.0],
                                                 'Factory': [3000.0, 10.0], 'Antimatter Condenser': [3999999999.0, 999999.0],
                                                 'Mine': [10000.0, 40.0]}, 1.15),
                             10000000000.0, cookie_clicker.strategy_expensive)
    print state
    print len(state.get_history())
    state.print_history()
