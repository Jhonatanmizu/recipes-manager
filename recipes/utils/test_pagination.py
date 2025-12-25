from unittest import TestCase

from utils.pagination import Pagination


class TestPagination(TestCase):
    def test_make_pagination_range(self) -> None:
        page_range = list(range(1, 6))
        current_page = 3
        quantity_pages_to_show = 5
        pagination = Pagination.make_pagination_range(
            page_range,
            current_page,
            quantity_pages_to_show=quantity_pages_to_show,
        )
        self.assertEqual([1, 2, 3, 4, 5], pagination)

    def test_basic_pagination_logic(self):
        items = list(range(1, 26))
        page_size = 10

        page_1 = items[0:page_size]
        self.assertEqual(page_1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        page_2 = items[page_size : page_size * 2]
        self.assertEqual(page_2, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

        page_3 = items[page_size * 2 : page_size * 3]
        self.assertEqual(page_3, [21, 22, 23, 24, 25])
