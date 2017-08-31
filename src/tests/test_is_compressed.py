import unittest
from common_helper_unpacking_classifier.uncompress_classifier import is_compressed


class TestIsCompressed(unittest.TestCase):

    def test_is_compressed(self):
        very_small_data = "AA"
        self.assertFalse(is_compressed(very_small_data))
        uncompressed_long_data = 16 * "this is an uncompressed text..."
        self.assertFalse(is_compressed(uncompressed_long_data))
        # simulated compress
        self.assertTrue(is_compressed(uncompressed_long_data, compress_entropy_threshold=0.4))


if __name__ == "__main__":
    unittest.main()