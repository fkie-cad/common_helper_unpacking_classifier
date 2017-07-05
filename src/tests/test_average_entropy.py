import unittest
from common_helper_unpacking_classifier.average_entropy import avg_entropy


class Test(unittest.TestCase):

    def test_avg_entropy(self):
        zero_entropy_data = 100 * b'\x00'
        self.assertEqual(avg_entropy(zero_entropy_data), 0)
        uncompressed_data = "this is not compressed"
        self.assertGreater(avg_entropy(uncompressed_data), 0.1)
        self.assertGreater(0.9, avg_entropy(uncompressed_data))

    def test_avg_entropy_error_cases(self):
        self.assertEqual(avg_entropy(b''), 0)


if __name__ == "__main__":
    unittest.main()
