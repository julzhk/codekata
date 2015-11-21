"""
Given two lists remove any occurance of the first list from the second list
"""

INTEMEDIARY_DELETION_MARKER = None

class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in self.filter(integer_list, values_list)]


    def filter(self, integer_list,  values_list):
        for i in integer_list:
            if i not in values_list:
                yield i


import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual
        # test.describe("Example Tests")
        l = List()

        integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
        values_list = [1, 3]
        test.assert_equals(l.remove_(integer_list, values_list), [2, 2, 4])

        integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
        values_list  = [1, 3, 4, 2]
        test.assert_equals(l.remove_(integer_list, values_list), [5, 6 ,7 ,8])

        integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
        values_list  = [2, 4, 3]
        test.assert_equals(l.remove_(integer_list, values_list), [8, 7, 6, 5, 1])
