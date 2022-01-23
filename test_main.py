from unittest import TestCase

from main import find_missed_num


class MissingNumberTestCase(TestCase):
    def test_without_first(self):
        numbers = [2, 3]
        self.assertEqual(find_missed_num(numbers), 1)

    def test_without_last(self):
        numbers = [1, 2]
        self.assertEqual(find_missed_num(numbers), 3)

    def test_without_middle(self):
        numbers = [1, 3]
        self.assertEqual(find_missed_num(numbers), 2)

    def test_without_middle_random_order(self):
        numbers = [3, 1, 5, 4]
        self.assertEqual(find_missed_num(numbers), 2)

    def test_len_2_without_first(self):
        numbers = [2]
        self.assertEqual(find_missed_num(numbers), 1)

    def test_len_2_without_last(self):
        numbers = [1]
        self.assertEqual(find_missed_num(numbers), 2)
