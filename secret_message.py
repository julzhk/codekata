import string
from collections import defaultdict
def find_secret_message(paragraph):
    answer = []
    seen = defaultdict(int)
    for word in paragraph.split(" "):
        word_to_check = word.lower().translate(None, string.punctuation.replace('-',''))
        if seen[word_to_check] == 1:
            answer.append(word_to_check)
        seen[word_to_check] += 1
    return ' '.join(answer)

import unittest

class TestFirst(unittest.TestCase):

    def test_first(self):
        test = self
        test.assert_equals = Test.assert_equals
        Test = self
        Test.assert_equals = Test.assert_equals

        paragraph = 'This is a test. this test is fun.'
        Test.assert_equals(find_secret_message(paragraph), 'this test is',"It should return lower case words"
                                      "                      in the orders in which you find the duplicate")
        paragraph = 'asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'
        Test.assert_equals(find_secret_message(paragraph), 'zxcv asdf qwer',"It should return lower case words ")
        Test.assert_equals(find_secret_message( 'zxcv asdf zxcv qwer asdf qwer zxcv'),'zxcv asdf qwer')
        Test.assert_equals(find_secret_message( "Testing for 'out moon good: sleeps CAT kills code sleeps "
                                                "think cat sleeps CHOCOLATE OUT eats! T-Rex! wants not? "
                                                "T-rex saves, in sun, never: wants! the? talks'),'zxcv asdf qwer"),
                                                'sleeps cat out t-rex wants')




pager = SearchPager(datacounts=[10,10,20,25], page_size=16)
r = pager.items(page=1)
Test.assert_equals(r[0], (0,3))
Test.assert_equals(r[1], (0,3))
Test.assert_equals(r[2], (0,3))
Test.assert_equals(r[3], (0,3))

r = pager.items(page=3)
Test.assert_equals(r[0], (8, 9))
Test.assert_equals(r[1], (8, 9))
Test.assert_equals(r[2], (8, 13))
Test.assert_equals(r[3], (8, 13))

r = pager.items(page=4)
Test.assert_equals(r[2], (14, 19))
Test.assert_equals(r[3], (14, 23))

r = pager.items(page=5)
Test.assert_equals(r[3], (24, 24))

---
pager = SearchPager(datacounts=[100,100,100] ,page_size=15)

r = pager.items(page=1)
Test.assert_equals(r[0],(0,4))
Test.assert_equals(r[1],(0,4))
Test.assert_equals(r[2],(0,4))

r = pager.items(page=2)
Test.assert_equals(r[0], (5, 9))
Test.assert_equals(r[1], (5, 9))
Test.assert_equals(r[2], (5, 9))

r = pager.items(page=20)
Test.assert_equals(r[0], (95, 99))
Test.assert_equals(r[1], (95, 99))
Test.assert_equals(r[2], (95, 99))

pager = SearchPager(datacounts=[10,20,25],page_size=15)
r = pager.items(page=1)
Test.assert_equals(r[0], (0,4))
Test.assert_equals(r[1], (0,4))
Test.assert_equals(r[2], (0,4))

r = pager.items(page=2)
Test.assert_equals(r[0], (5, 9))
Test.assert_equals(r[1], (5, 9))
Test.assert_equals(r[2], (5, 9))

r = pager.items(page=3)
# should add up to a pages size of 15!
Test.assert_equals(r[1], (10, 17))
Test.assert_equals(r[2], (10, 16))

r = pager.items(page=4)
# col 1 only up to count 20
Test.assert_equals(r[1], (18, 19))
# should add up to a pages size of 15, but we only have 25 col 2s!
Test.assert_equals(r[2], (17, 24))
