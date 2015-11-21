ALPHANUMERICAL_DIGITS= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BIN_DIGITS= ALPHANUMERICAL_DIGITS[0:2]
OCT_DIGITS= ALPHANUMERICAL_DIGITS[0:8]
DECIMAL_DIGITS= ALPHANUMERICAL_DIGITS[0:10]
HEX_DIGITS= ALPHANUMERICAL_DIGITS[0:16]
ALL_LOWER= ALPHANUMERICAL_DIGITS[10:36]
ALL_UPPER= ALPHANUMERICAL_DIGITS[36:]
ALPHA_DIGITS= ALPHANUMERICAL_DIGITS[10:]

def convert_from(input, source):
    """
    Convert from one base to digit
    :param input: String
    :param source: all digits for a base
    :return: Int
    """
    base = len(source)
    result = 0
    for power, i in enumerate(input[::-1]):
        result +=source.index(i) * pow(base, power)
    return result

def convert_to(input, target):
    """
    Convert from integer to target-base string representation
    :param input: Integer
    :param target: all digits for a base
    :return: string representation in Base n
    """
    result = ''
    base = len(target)
    while True:
        result = '%s%s' % (str(target[input % base]),result)
        input  = input // base
        if not (input > 0):
            break
    return result

def convert(input, source, target):
    """
    Convert from one base to another
    :param input: all base digits:from
    :param source: source chars
    :param target: all base digits:to
    :return: results as string
    """
    decimal = convert_from(input = input, source=source)
    return convert_to(input=decimal,target=target)

import unittest

class TestFirst(unittest.TestCase):

    def testFirst(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        test.assert_equals(ALL_LOWER, 'abcdefghijklmnopqrstuvwxyz')
        test.assert_equals(ALL_UPPER, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        test.assert_equals(ALPHA_DIGITS, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        test.assert_equals(convert("15", DECIMAL_DIGITS, BIN_DIGITS), '1111', '"15" dec -> bin')
        test.assert_equals(convert_from("15", DECIMAL_DIGITS), 15, )
        test.assert_equals(convert_from("15", OCT_DIGITS), 13, )
        test.assert_equals(convert_from("10", BIN_DIGITS), 2, )
        test.assert_equals(convert_from("110", BIN_DIGITS), 6, )
        test.assert_equals(convert_from("100", BIN_DIGITS), 4, )

        test.assert_equals(convert_to(4, BIN_DIGITS), "100")
        test.assert_equals(convert_to(8, OCT_DIGITS), "10")
        test.assert_equals(convert_to(9, OCT_DIGITS), "11")
        test.assert_equals(convert_to(10, OCT_DIGITS), "12")
        test.assert_equals(convert_to(11, OCT_DIGITS), "13")

        test.assert_equals(convert("15", DECIMAL_DIGITS, OCT_DIGITS), '17', '"15" dec -> oct')
        test.assert_equals(convert("1010", BIN_DIGITS, DECIMAL_DIGITS), '10', '"1010" bin -> dec')
        test.assert_equals(convert("1010", BIN_DIGITS, HEX_DIGITS), 'a', '"1010" bin -> hex')
        test.assert_equals(convert("0", DECIMAL_DIGITS, ALPHA_DIGITS), 'a', '"0" dec -> alpha')
        test.assert_equals(convert("27", DECIMAL_DIGITS, ALL_LOWER), 'bb', '"27" dec -> alpha_lower')
        test.assert_equals(convert("hello", ALL_LOWER, HEX_DIGITS), '320048', '"hello" alpha_lower -> hex')
        test.assert_equals(convert("SAME", ALL_UPPER, ALL_UPPER), 'SAME', '"SAME" alpha_upper -> alpha_upper')
