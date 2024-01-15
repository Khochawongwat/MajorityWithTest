import unittest

from main import majority

class TestMajority(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(majority([]), None)

    def test_no_majority(self):
        self.assertEqual(majority([1, 2, 3, 4, 5]), None)

    def test_majority_exists(self):
        self.assertEqual(majority([1, 1, 2, 1, 3]), 1)

    def test_majority_with_same_counts(self):
        self.assertEqual(majority([1, 1, 2, 2]), None)

    def test_large_list(self):
            self.assertEqual(majority([1]*1000 + [2]*500), 1)

    def test_close_counts(self):
        self.assertEqual(majority([1]*1000 + [2]*500), 1)

if __name__ == '__main__':
    unittest.main()