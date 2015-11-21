"""
Bob is preparing to pass IQ test.
The most frequent task in this test is to find out which one of the given numbers differs from the others.
Bob observes that one number usually differs from the others in evenness.
Help Bob to check his answers: he needs a program that among the given numbers finds one that is different in evenness,
and return the position of this number.

"""
def count_parity(nums,even):
    rem = 0 if even else 1
    #     parity is maths language for even/odd-ness
    return sum([1 for i in nums if i%2 == rem ])

def get_first_of_parity(nums, even):
    rem = 1 if even else 0
    for pos, i in enumerate(nums, start=1):
        if i % 2 == rem:
            return pos


def iq_test(numbers_string):
    nums = [int(i) for i in numbers_string.split(' ')]
    evens = count_parity(nums,even=True)
    odds = count_parity(nums,even=False)
    check_even = (evens > odds)
    return get_first_of_parity(nums,even=check_even)



import unittest


class TestFirst(unittest.TestCase):
    def test_hekpers(self):
        self.assertEqual(count_parity([1,2,3],even=True),1)
        self.assertEqual(count_parity([1,2,3,4],even=True),2)
        self.assertEqual(count_parity([1,2,3],even=False),2)
        self.assertEqual(count_parity([1,2,3,4],even=False),2)
    def test_first(self):
        Test = self
        Test.assert_equals = self.assertEqual
        Test.assert_equals(iq_test("2 4 7 8 10"),3)
        Test.assert_equals(iq_test("1 2 2"), 1)
        Test.assert_equals(iq_test("1 2 1 1") , 2)
        # // Second number is even, while the rest of the numbers are odd
