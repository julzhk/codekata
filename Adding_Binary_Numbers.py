"""
Add two binary string *without* converting them to numerical representations!
"""

from collections import deque

BINARY_RESULTS= {
    ('0','0','0'): ('0','0'),
    ('0','0','1'): ('1','0'),
    ('0','1','1'): ('0','1'),
    ('1','1','1'): ('1','1'),
}

def add_binary_digits(a, b, column_index, carry):
    """
    Given an augend and addend (numbers to add!) and col/carryover values
    give a result for the column & a carryover digit
    :param a: augend String {'0'|'1'}
    :param b: addend String {'0'|'1'}
    """
    r = tuple(sorted([
                a[column_index - 1] ,
                b[column_index - 1],
                carry
    ]))
    result,carry = BINARY_RESULTS[r]
    return carry, result


def trim_preceeding_zeroes(s):
    bin_string =deque(s)
    for i in s:
        if bin_string[0] == '0':
            bin_string.popleft()
    return ''.join(bin_string)


def add(a,b):
    carry = '0'
    maxlen = max(len(a),len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    endresult = ''
    for column in range(maxlen,0,-1):
        carry, result = add_binary_digits(a, b, column, carry)
        endresult = '%s%s' % (result, endresult)
    endresult = '%s%s' % (carry, endresult)
    r= ''.join(trim_preceeding_zeroes(endresult))
    r = coerce_blanks_show_as_zero(r)
    return r


def coerce_blanks_show_as_zero(r):
    if r == '':
        r = '0'
    return r


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        Test.assert_equals(trim_preceeding_zeroes('0001'),'1')
        Test.assert_equals(add('111','10'),'1001')
        Test.assert_equals(add('1101','101'), '10010')
        Test.assert_equals(add('1101','10111') , '100100')
        Test.assert_equals(add('111','10'),'1001')
        Test.assert_equals(add('1101','101'),'10010')
        Test.assert_equals(add('1101','10111'),'100100')
        Test.assert_equals(add('10111','001010101'),'1101100')
        Test.assert_equals(add('00','0'),'0')