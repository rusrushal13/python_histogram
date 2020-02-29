import unittest
from utilities import (count_in_between,
                       fetch_min_max_bucket_sizes)

from histogram import (print_histogram)


class TestHistogram(unittest.TestCase):
    """
    Testing module for Histogram.

    ARGS:
    """

    def test_one_count_in_between(self):
        """
        Unittest for the count in between.

        ARGS:
        """
        self.assertEqual(count_in_between([1, 2, 3, 4, 5], 1, 5), 4)

    def test_two_count_in_between(self):
        """
        Unittest for the count in between.

        ARGS:
        """
        self.assertEqual(count_in_between([1, 2, 3, 4, 5], 1, 6), 5)

    def test_three_count_in_between(self):
        """
        Unittest for the count in between.

        ARGS:
        """
        self.assertEqual(count_in_between([1, 2, 3, 4, 5], 10, 15), 0)

    def test_fourth_count_in_between(self):
        """
        Unittest for the count in between fail.

        ARGS:
        """
        self.assertFalse(count_in_between([1, 2, 3, 4, 5], 10, 15), 1)

    def test_fetch_min_max_bucket_sizes(self):
        """
        Unittest for the fetch minimum maximum buckets sizes.

        ARGS:
        """
        inputs = [1, 2, 3, 4, 5]
        bucket_size = 1
        min_bucket_size, max_bucket_size = fetch_min_max_bucket_sizes(inputs, bucket_size)
        self.assertEqual(min_bucket_size, 1)
        self.assertEqual(max_bucket_size, 6)

if __name__ == '__main__':
    unittest.main()
