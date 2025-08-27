import os
from common_helper_unpacking_classifier.get_size import get_binary_size_without_padding


def test_get_bin_size_without_padding():
    no_padding = b'abcdefgt'
    assert get_binary_size_without_padding(no_padding) == len(no_padding)
    with_padding = os.urandom(4096) + b'\x00' * 1024 + os.urandom(4096)
    assert get_binary_size_without_padding(with_padding) == 4096*2
