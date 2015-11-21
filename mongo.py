"""
Implement a function to check if a Mongo database ID is valid
"""

from datetime import datetime
from collections import namedtuple

Mongo_id = namedtuple('Mongo_id', ['timestamp', 'machine_id', 'process_id', 'counter'])


class Mongo(object):
    MONGO_ID_LEN = 24

    @classmethod
    def length_valid(cls, s):
        return len(str(s)) == Mongo.MONGO_ID_LEN

    @classmethod
    def hex_lowercase_valid(cls, s):
        for c in s:
            if not (c.islower() or c.isdigit()):
                return False
        return True

    @classmethod
    def is_valid(cls, s):
        try:
            if not (cls.length_valid(s) and cls.hex_lowercase_valid(s)):
                return False
            cls.hex_to_decimal(s)
            return True
        except (TypeError, ValueError):
            return False

    @classmethod
    def hex_to_decimal(cls, ts):
        ts = int(ts, 16)
        return ts

    @classmethod
    def get_id_elements(cls, s):
        return Mongo_id(s[:8], s[9:15], s[16:20], s[21:])

    @classmethod
    def get_timestamp(cls, s):
        if not cls.is_valid(s):
            return False
        id_elements = Mongo.get_id_elements(s)
        ts = cls.hex_to_decimal(id_elements.timestamp)
        r = datetime.utcfromtimestamp(ts)
        return r


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        test.assert_equals = self.assertEqual
        Test = self
        Test.assert_equals = self.assertEqual
        from datetime import datetime

        test.assert_equals(Mongo.is_valid(False), False)
        test.assert_equals(Mongo.is_valid([]), False)
        test.assert_equals(Mongo.is_valid(1234), False)
        test.assert_equals(Mongo.is_valid('123476sd'), False)
        test.assert_equals(Mongo.is_valid('507f1f77bcf86cd79943901'), False)
        test.assert_equals(Mongo.is_valid('507f1f77bcf86cd799439016'), True)

        test.assert_equals(Mongo.get_timestamp(False), False)
        test.assert_equals(Mongo.get_timestamp([]), False)
        test.assert_equals(Mongo.get_timestamp(1234), False)
        test.assert_equals(Mongo.get_timestamp('123476sd'), False)
        test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd79943901'), False)
        test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd799439016'), datetime(2012, 10, 17, 21, 13, 27))
        # test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd799439011'),datetime(2012,10,Oct 17 2012 21:13:27 GMT-0700 (Pacific Daylight Time)
        test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cz799439011'), False)  # False
        test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd79943901'), False)  # False
        test.assert_equals(Mongo.get_timestamp('111111111111111111111111'),datetime(1979, 1, 28, 0, 25, 53)) # Sun Jan 28 1979 00:25:53 GMT-0800 (Pacific Standard Time)
        test.assert_equals(Mongo.get_timestamp(111111111111111111111111), False)
        test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cD799439011'), False)
        test.assert_equals(Mongo.get_timestamp('52fefe6cb0091856db00030e'), datetime(2014, 2, 15, 5, 43, 8))
