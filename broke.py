"""
Convert infix maths notation to post fix:
1+1 -> 1 1 +
"""

import string

def get_precedence(op):
    op_precedence = [ '(',
                     '+-',
                     '*/',
                     ]
    for i, operators in enumerate(op_precedence):
        if op in operators:
            return i

def to_postfix (infix):
    """Convert infix to postfix"""
    output = []
    op_queue = []
    for i in infix:
        if (i in string.digits) or (i == '('):
            output.append(i)
        elif i == ')' :
            while len(op_queue) and op_queue[-1] != '(':
                m = op_queue.pop(-1)
                output.append(m)
        else:
    #         is operator
            op_queue.append(i)
            try:
                a,b = op_queue[-1],op_queue[-2]
                a_pres, b_pres = get_precedence(a), get_precedence(b)
                while len(op_queue) and a_pres < b_pres :
                    output.append(op_queue.pop(-1))
                    a,b = op_queue[-1],op_queue[-2]
                    a_pres, b_pres = get_precedence(a), get_precedence(b)

            except IndexError:
                pass
    r = ''.join(output + op_queue[::-1])
    return r


import unittest

class TestFirst(unittest.TestCase):

    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        Test.assert_equals(to_postfix("2+7"), "27+")
        Test.assert_equals(to_postfix("2+7+9"), "279++")
        Test.assert_equals(to_postfix("2+7*5"), "275*+")

        # is '3371*+/' ' not "33*71+/"
        Test.assert_equals("33*71+/", to_postfix("3*3/(7+1)"))
        Test.assert_equals(to_postfix("5+(6-2)*9+3^(7-1)"), "562-9*+371-^+")
        Test.assert_equals(to_postfix("(5-4-1)+9/5/2-7/1/7"), "54-1-95/2/+71/7/-")
