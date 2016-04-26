import string
from operator import ge as greater_than_or_equal, gt as greater_than
from collections import deque

OPERATOR_PRECEDENCE = {
    '(':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3,
}

RIGHT_ASSOCIATIVE_OPERATORS = '^'
LEFT_ASSOCIATIVE_OPERATORS = '+-/*'


def pop_operator_queue(operators, output, token):
    """
    Pop operators from the queue. left associative and right assoc fns are compared slightly differently!
    :type operators: deque
    :type output: deque
    :type token: str
    :return: None
    """
    comparison_op = greater_than if token in RIGHT_ASSOCIATIVE_OPERATORS else greater_than_or_equal
    while operators and comparison_op(OPERATOR_PRECEDENCE[operators[-1]], OPERATOR_PRECEDENCE[token]):
        output.append(operators.pop())
    operators.append(token)

def to_postfix (infix):
    infix = deque(infix)
    output = deque()
    operators = deque()
    while infix:
        token = infix.popleft()
        if token in string.digits:
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                    output.append(operators.pop())
            output.append(operators.pop())
        elif token in LEFT_ASSOCIATIVE_OPERATORS:
            # >=
            pop_operator_queue(operators, output, token)
        elif token in RIGHT_ASSOCIATIVE_OPERATORS:
            # >
            pop_operator_queue(operators, output, token)
    while operators:
        output.append(operators.pop())
    return ''.join(output).replace('(','')



import unittest
class TestFirst(unittest.TestCase):
    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        Test.assert_equals(to_postfix("2+7"), "27+")
        Test.assert_equals(to_postfix("2+7+9"), "27+9+")
        Test.assert_equals(to_postfix("2+7*5"), "275*+")
        Test.assert_equals(to_postfix("99*6+"), "996*+")
        #'337/*1+'
        Test.assert_equals("33*8/", to_postfix("3*3/8"))
        Test.assert_equals("33*71+/", to_postfix("3*3/(7+1)"))
        Test.assert_equals("562-9*+", to_postfix("5+(6-2)*9"))
        Test.assert_equals("562-9*+36^+", to_postfix("5+(6-2)*9+3^6"))
        Test.assert_equals("562-9*+371-^+", to_postfix("5+(6-2)*9+3^(7-1)"))
        Test.assert_equals(to_postfix("(5-4-1)+9/5/2-7/1/7"), "54-1-95/2/+71/7/-")

