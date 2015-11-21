"""
implement a compount interest calculator, but with a difference:
given an interest rate, return how many years it will take to hit a target sum
"""

# Let P be the Principal = 1000.00
#  Let I be the Interest Rate = 0.05
#  Let T be the Tax Rate = 0.18
#  Let D be the Desired Sum = 1100.00

# After 1st Year -->  P = 1041.00
# After 2nd Year -->  P = 1083.86
# After 3rd Year -->  P = 1128.30

from math import log, ceil

def calculate_years(principal, interest, tax, desired):
    r = (log(float(desired) / principal, 1 + (interest * (1 - tax))))
    r = ceil(r)
    return r


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual


        Test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
        Test.assert_equals(calculate_years(1000,0.01625,0.18,1200), 14)
        Test.assert_equals(calculate_years(1000,0.05,0.18,1000), 0)
