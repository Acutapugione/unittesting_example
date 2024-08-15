"""Simple tests for `main.py`"""

from unittest import TestCase

from main import book_the_table


class TestBooking(TestCase):
    """Test case for booking business logic"""

    def setUp(self) -> None:  # __enter__
        self.tables = [
            {
                "id": 1,
                "pos": 2,
                "is_free": True,
            },
            {
                "id": 2,
                "pos": 2,
                "is_free": False,
            },
        ]
        return super().setUp()

    def test_book_the_table(self) -> None:
        """test `book_the_table` function"""
        # self.assertEqual(2, 3)
        self.assertIsNone(book_the_table(self.tables, 1))
        with self.assertRaises(Exception):
            book_the_table(self.tables, 2)

    def test_access_errors(self) -> None:
        """test data access errors"""

        with self.assertRaises(IndexError):
            print(self.tables[2])

    # def tearDown(self) -> None:  # __exit__
    #     return super().tearDown()
