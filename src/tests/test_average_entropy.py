from pathlib import Path

import pytest
import math

from common_helper_unpacking_classifier.average_entropy import avg_entropy

test_data_dir = Path(__file__).parent / "data"


def test_avg_entropy():
    zero_entropy_data = 100 * b"\x00"
    assert math.isclose(avg_entropy(zero_entropy_data), 0.0)
    uncompressed_data = b"this is not compressed"
    assert 0.9 > avg_entropy(uncompressed_data) > 0.1


def test_avg_entropy_error_cases():
    assert math.isclose(avg_entropy(b""), 0.0)


@pytest.mark.parametrize(
    ("input_file_name", "expected_output"),
    [
        ("0_entropy", 0.0),
        ("max_entropy", 1.0),
    ],
)
def test_avg_entropy_from_file(input_file_name, expected_output):
    zero_entropy_file = test_data_dir / input_file_name
    assert avg_entropy(zero_entropy_file) == expected_output
    with open(zero_entropy_file, "rb") as fp:
        assert math.isclose(avg_entropy(fp), expected_output)
