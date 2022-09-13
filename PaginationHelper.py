from itertools import izip_longest

ERROR_COUNT = -1


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def grouper(self, fillvalue=None):
        # see 'grouper' in https://docs.python.org/2/library/itertools.html#recipes
        # "Collect data into fixed-length chunks or blocks"
        args = [iter(self.collection)] * self.items_per_page
        return izip_longest(fillvalue=fillvalue, *args)

    def item_count(self):
        return len(self.collection)

    def has_partial_page_of_results(self):
        return self.item_count() % self.items_per_page != 0

    def page_count(self):
        number_of_partial_pages = 1 if self.has_partial_page_of_results() else 0
        return (self.item_count() / self.items_per_page) + number_of_partial_pages

    def page_items(self, page_index):
        p = self.grouper()
        page_content = []
        for page in range(0, page_index + 1):
            page_content = p.next()
        return [p for p in page_content if p is not None]

    def page_item_count(self, page_index):
        if page_index < 0:
            return self.items_per_page
        try:
            return len(self.page_items(page_index=page_index))
        except StopIteration:
            return ERROR_COUNT

    def page_index(self, item_index):
        if item_index == 0 and self.item_count():
            return 0
        if 0 <= item_index < self.item_count():
            return item_index / self.items_per_page
        else:
            return ERROR_COUNT


import unittest


class TestFirst(unittest.TestCase):
    def test_first(self):
        test = self
        Test = self
        test.assert_equals = Test.assertEqual
        Test.assert_equals = Test.assertEqual

        helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        Test.assertEqual(helper.page_count(), 2)
        Test.assertEqual(helper.item_count(), 6)
        Test.assertEqual(helper.page_item_count(0), 4)
        Test.assertEqual(helper.page_item_count(1), 2)
        Test.assertEqual(helper.page_item_count(2), -1)

        Test.assertEqual(helper.page_index(5), 1)
        Test.assertEqual(helper.page_index(2), 0)
        Test.assertEqual(helper.page_index(8), -1)
        Test.assertEqual(helper.page_index(0), 0)
        Test.assertEqual(helper.page_index(1), 0)
        Test.assertEqual(helper.page_index(20), -1)
        Test.assertEqual(helper.page_index(-10), -1)

        collection = range(1, 25)
        helper = PaginationHelper(collection, 10)

        Test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
        Test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
        Test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')

        helper = PaginationHelper([], 4)
        Test.assertEqual(helper.page_count(), 0)
        Test.assertEqual(helper.item_count(), 0)
        Test.assertEqual(helper.page_index(-10), -1)
        Test.assertEqual(helper.page_index(2), -1)
        Test.assertEqual(helper.page_index(0), -1)

        helper = PaginationHelper([2]*12, 9)
        Test.assertEqual(helper.page_index(-1), -1)

# Testing .page_item_count() method for 3 elements, 4 elements per page, page number -3
        Test.assertEqual(helper.page_item_count(-1), 9)

        helper = PaginationHelper([1]*8, 8)
        Test.assertEqual(helper.page_item_count(-3), 4)
# Testing .page_item_count() method for 8 elements, 8 elements per page, page number 0
