"""
Take any positive integer n. If n is even divide it by 2. If n is odd multiply it by 3 and add 1.
Repeat the process (aka: "Half Or Triple Plus One") indefinitely.
It's thought that no matter what number you start with you will always eventually reach 1.
Create a function that returns the number of steps taken to reach 1.
More information : https://en.wikipedia.org/wiki/Collatz_conjecture

For instance:
starting with n = 6 the sequence is 6->3->10->5->16->8->4->2->1.
Hence, HOTPO(6) == 8
n = 13 the sequence is 13->40->20->10->5->16->8->4->2->1.
Hence, HOTPO(13) == 9



"""

def is_even(n):
    return n % 2 == 0

def hotpo(n,total=0):
    if 0 < n <=1:
        return total
    else:
        if is_even(n):
            return hotpo(n /2 , total= total + 1)
        else:
            return hotpo((n*3)+1  , total= total + 1)

import unittest
class TestStringMethods(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self

        self.assertEqual(hotpo(2), 1)
        self.assertEqual(hotpo(3), 7)
        self.assertEqual(hotpo(1), 0)
        self.assertEqual(hotpo(4), 2)
        self.assertEqual(hotpo(5), 5)
        self.assertEqual(hotpo(6), 8)
        self.assertEqual(hotpo(7), 16)
        self.assertEqual(hotpo(8), 3)
        self.assertEqual(hotpo(9), 19)
        self.assertEqual(hotpo(10), 6)
        self.assertEqual(hotpo(11), 14)
        self.assertEqual(hotpo(12), 9)
        self.assertEqual(hotpo(13), 9)
        self.assertEqual(hotpo(14), 17)

        self.assertEqual(hotpo(20), 7)
        self.assertEqual(hotpo(40), 8)
        self.assertEqual(hotpo(60), 19)
        self.assertEqual(hotpo(80), 9)
        self.assertEqual(hotpo(100), 25)
        self.assertEqual(hotpo(120), 20)
        self.assertEqual(hotpo(140), 15)


        self.assertEqual(hotpo(6), 8)
        self.assertEqual(hotpo(13), 9)

        self.assertEqual(hotpo(3), 7)

