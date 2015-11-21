"""
Implement a simple state machine, which will be given a list of 1|0 commands.

Have it follow some state change rules:
# q1 moves to q2 when given a 1,
# q1 stays at q1 when given a 0.
# q2 moves to q3 when given a 0,
# q2 stays at q2 when given a 1.
# q3 moves to q2 when given a 0 or 1.

"""
INITIAL_STATE = 'q1'
ACCEPTED_STATE = 'q2'
UNACCEPTED_STATE = 'q3'

def state_from_q1(state_change):
    """
    >>> state_from_q1("1")
    'q2'
    >>> state_from_q1("0")
    'q1'
    >>> state_from_q1("2")
    'q1'
    """
    return ACCEPTED_STATE if state_change == "1" else INITIAL_STATE

def state_from_q2(state_change):
    """
    >>> state_from_q2("0")
    'q3'
    >>> state_from_q2("1")
    'q2'
    >>> state_from_q2("2")
    'q3'
    """
    return ACCEPTED_STATE if state_change == "1" else UNACCEPTED_STATE

def state_from_q3(state_change):
    """
    >>> state_from_q3("0")
    'q2'
    >>> state_from_q3("1")
    'q2'
    >>> state_from_q3("2")
    'q2'
    """
    return ACCEPTED_STATE


class Automaton(object):

    def __init__(self):
        self.state_change_map = {
            INITIAL_STATE: state_from_q1,
            ACCEPTED_STATE: state_from_q2,
            UNACCEPTED_STATE: state_from_q3
        }
        self.state = INITIAL_STATE

    def end_in_accepted_state(self):
        return  self.state is ACCEPTED_STATE

    def read_commands(self, commands):
        for state_change in commands:
            fn = self.state_change_map[self.state]
            self.state = fn(state_change)
        return self.end_in_accepted_state()

my_automaton = Automaton()



import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        Test.assert_equals(my_automaton.read_commands(["1"]), True)
        Test.assert_equals(my_automaton.read_commands(["1", "0", "0", "1"]), True)
        Test.assert_equals(my_automaton.read_commands(["1", "0", "0", "1", "0"]),False)
        Test.assert_equals(my_automaton.read_commands(["1", "0", "0", "1", "0","1"]),True)
