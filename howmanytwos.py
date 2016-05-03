# how many times can a number be divided by 2?
#  ie 24/2=>12. 12/2=>6, 6/2=>3 so 24 is divide by 2 three times.

def two_count(n):
    i = 0
    while not n % 2:
        i += 1
        n /= 2
    return i



import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        test.assert_equals(two_count(24), 3)
        test.assert_equals(two_count(17280), 7)
        test.assert_equals(two_count(222222222222), 1)
        test.assert_equals(two_count(256),8)