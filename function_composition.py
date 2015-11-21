"""
Use 1st order functions to create a simple maths DSL
"""

add1 = lambda a: a+1
this = lambda a: a
double = lambda a: a*2

def summa(*args):
    return sum(list(args))


def compose(f,g):
    def fn(*args, **kwargs):
        return f(g(*args, **kwargs))
    return fn


import unittest
class TestFirst(unittest.TestCase):
    def test_first(self):
        # test.expect( compose(add1,this)(0) == 1 )
        self.assertEqual(compose(add1, this)(0), 1)
        self.assertEqual(compose(add1, this)(1), 2)
        self.assertEqual(compose(add1, double)(1), 3)
        self.assertEqual(compose(double, double)(1), 4)
        self.assertEqual(compose(double, summa)(3,4), 14)
        self.assertEqual(compose(double, summa)(2,3,4), 18)