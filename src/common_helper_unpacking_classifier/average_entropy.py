import logging
import sys

from entropy import shannon_entropy as shannon_entropy_natano

from .chi_square_test import chi_square_test
from .g_test import g_test
from .helper import _calculate_end_of_block
from .shannon_entropy import shannon_entropy_byte


BLOCKSIZE = 256


def avg_entropy(input_data, block_size=BLOCKSIZE, entropy_function=shannon_entropy_natano):
    """
    Calculates the average entropy of input_data regarding block_size

    :param input_data: input data
    :type file_path: bytes
    :param block_size: shannon block size in bytes
    :type block_size: int
    :return: float
    """
    offset = 0
    entropy_sum = 0
    number_of_blocks = 0
    while offset < len(input_data):
        end_of_block = _calculate_end_of_block(offset, block_size, len(input_data))
        current_block = input_data[offset:end_of_block]
        entropy_sum += entropy_function(current_block) * (len(current_block) / block_size)
        offset = end_of_block
        number_of_blocks += (len(current_block) / block_size)
    try:
        return entropy_sum / number_of_blocks
    except Exception as e:
        logging.warning("Could not calculate entropy: {} {}".format(sys.exc_info()[0].__name__, e))
        return 0


def avg_shannon_entropy(input_data, block_size=BLOCKSIZE):
    return avg_entropy(input_data, block_size=block_size, entropy_function=shannon_entropy_natano)


def avg_shannon_entropy_byte(input_data, block_size=BLOCKSIZE):
    return avg_entropy(input_data, block_size=block_size, entropy_function=shannon_entropy_byte)


def avg_chi_square_test(input_data, block_size=BLOCKSIZE):
    return avg_entropy(input_data, block_size=BLOCKSIZE, entropy_function=chi_square_test)


def avg_g_test(input_data, block_size=BLOCKSIZE):
    return avg_entropy(input_data, block_size=block_size, entropy_function=g_test)
