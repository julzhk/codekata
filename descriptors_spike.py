class Quantity(object):
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem(object):
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        if initval>0:
            self.val = initval
            self.name = name
        else:
            raise ValueError('no cannot set')

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        if val>0:
            self.val = val
        else:
            raise ValueError('no cannot! ')

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        try:
            truffle = LineItem('White Truffle', 100, 0)
            print truffle.subtotal()
        except ValueError:
            print 'throw correct exception'

    def test2(self):

        m = MyClass()
        print m.x
        print m.y
        try:
            m.x=0
        except ValueError:
            print 'correct error'
        print m.x
