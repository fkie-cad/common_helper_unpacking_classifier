import unittest
import os
from common_helper_unpacking_classifier.get_size import get_file_size, get_binary_size_without_padding


class TestGetSize(unittest.TestCase):

    def test_get_file_size(self):
        none_existing_file = '/foo/nonexisting'
        self.assertEqual(get_file_size(none_existing_file), 0)
        existing_file = os.path.abspath(__file__)
        self.assertGreater(get_file_size(existing_file), 1)

    def test_get_bin_size_without_padding(self):
        no_padding = b'abcdefgt'
        self.assertEqual(get_binary_size_without_padding(no_padding), len(no_padding))
        with_padding = b'abcd' + 4 * b'\x00' + b'abcd'
        self.assertEqual(len(with_padding), 12)
        self.assertEqual(get_binary_size_without_padding(with_padding), 8)
