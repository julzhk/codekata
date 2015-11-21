from math import sqrt

class VectorIncompatibleException(Exception):
    pass

def vectors_compatible(func):
    def inner(*args, **kwargs):
        vector_dimensions = len(args[0].vectors)
        for arg in args:
            if vector_dimensions != len(arg.vectors):
                raise VectorIncompatibleException()
        return func(*args, **kwargs)
    return inner


class Vector(object):
    def __init__(self, vectors):
        self.vectors = vectors

    def vector_operation(self,b, fn):
        return Vector([fn(i[0] , i[1]) for i in zip(self.vectors, b.vectors)])

    @vectors_compatible
    def add(self,b):
        return self.vector_operation(b,lambda x, y : x + y)

    @vectors_compatible
    def subtract(self,b):
        return self.vector_operation(b,lambda x, y : x - y)


    def toString(self):
        return self.__str__()

    @vectors_compatible
    def dot(self,b):
        multipled = self.vector_operation(b,lambda x, y : x * y)
        return sum(multipled.vectors)

    def __str__(self):
        return str(tuple(self.vectors)).replace(' ','')

    def __eq__(self, b):
        return self.vectors == b.vectors

    def equals(self,b):
        return self.__eq__(b)

    def norm(self):
        squared = self.vector_operation(self,lambda x, y : x * y)
        r = sum(squared.vectors)
        return sqrt(r)




import unittest


class TestFirst(unittest.TestCase):

    def test_first(self):
        test = self
        test.assert_equals = self.assertEqual
        test.expect = self.assertEqual
        Test = self
        Test.assert_equals = self.assertEqual
        a = Vector([1,2])
        b = Vector([3,4])
        test.expect(a.add(b), Vector([4,6]))
        test.expect(a.toString() , '(1,2)')
        c = Vector([3,4])
        self.assertEqual (b.toString(), c.toString())



    def test_second(self):
        test = self
        test.assert_equals = self.assertEqual
        test.expect = self.assertEqual
        Test = self
        Test.assert_equals = self.assertEqual
        a = Vector([1,2,3])
        b = Vector([3,4,5])
        c = Vector([5,6,7,8])
        test.expect(a.add(b),Vector([4,6,8]))
        test.expect(a.subtract(b), Vector([-2,-2,-2]))
                            # 1*3+2*4+3*5 = 26
        test.expect(a.dot(b), 26)
        from math import sqrt
        test.expect(a.norm() , sqrt(14))
        # sqrt(1^2+2^2+3^2)
        with self.assertRaises(Exception):
            a.add(c)


