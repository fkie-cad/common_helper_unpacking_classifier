import logging
import os
import sys

from common_helper_files import get_binary_from_file
from entropython import metric_entropy as entropy

from .helper import _calculate_end_of_block

BLOCKSIZE = 4
PADDING_ENTROPY_THRESHOLD = 0.1


def get_file_size(file_path: str) -> int:
    '''
    Returns the size of file in bytes. Returns zero on error.

    :param file_path: path to file
    :return: the size of file as number of bytes
    '''
    try:
        return os.path.getsize(file_path)
    except Exception as err:
        logging.error('Could not get file size: {} {}'.format(sys.exc_info()[0].__name__, err))
        return 0


def get_file_size_without_padding(file_path: str) -> int:
    '''
    Returns the size of file in bytes minus size of padding areas.

    :param file_path: path to file
    :type file_path: str
    :return: int
    '''
    file_data = get_binary_from_file(file_path)
    return get_binary_size_without_padding(file_data)


def get_binary_size_without_padding(data: bytes, blocksize: int = BLOCKSIZE,
                                    padding_entropy_threshold: float = PADDING_ENTROPY_THRESHOLD) -> int:
    '''
    Returns the size of input_data in bytes minus size of padding areas.

    :param data: input data
    :param blocksize: block-size regarding padding detection
    :param padding_entropy_threshold: shannon entropy threshold regarding padding detection
    :return: the size of input_data without padding
    '''
    original_size = len(data)
    padding_size = 0
    offset = 0
    while offset < original_size:
        end_of_block = _calculate_end_of_block(offset, blocksize, original_size)
        if entropy(data[offset:end_of_block]) <= padding_entropy_threshold:
            padding_size += blocksize
        offset = end_of_block
    return original_size - padding_size
