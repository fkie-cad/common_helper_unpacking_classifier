import logging
import sys
from typing import Callable

from entropython import metric_entropy, shannon_entropy

from .helper import _calculate_end_of_block

BLOCKSIZE = 256


def avg_entropy(input_data: bytes, block_size: int = BLOCKSIZE, entropy_function: Callable = metric_entropy) -> float:
    '''
    Calculates the average entropy of input_data regarding block_size

    :param input_data: input data
    :param block_size: shannon block size in bytes
    :param entropy_function: the function to use for entropy calculation
    :return: float
    '''
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
    except Exception as err:
        logging.warning('Could not calculate entropy: {} {}'.format(sys.exc_info()[0].__name__, err))
        return 0.0


def avg_shannon_entropy(input_data, block_size=BLOCKSIZE):
    return avg_entropy(input_data, block_size=block_size, entropy_function=metric_entropy)


def avg_shannon_entropy_byte(input_data, block_size=BLOCKSIZE):
    return avg_entropy(input_data, block_size=block_size, entropy_function=shannon_entropy)
