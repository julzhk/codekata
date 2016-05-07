# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# ProjectEuler.net
MULTIPLE_TARGETS = [3,5]

def sieve(number):
    result = set()
    for i in range(1,number):
        for fact in MULTIPLE_TARGETS:
            if i % fact == 0:
                result.add(i)
                continue
    return result



def solution(number):
    return sum(sieve(number))


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

    def test_sieve(self):
        self.assertEquals(sieve(10),set([3,5,6,9]))
        self.assertEquals(sieve(9),set([3,5,6]))