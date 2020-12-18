import logging
import os
import sys

from common_helper_files import get_binary_from_file

from .helper import _calculate_end_of_block
from .shannon_entropy import normalized_shannon_byte_entropy as entropy

BLOCKSIZE = 4
PADDING_ENTROPY_THRESHOLD = 0.1


def get_file_size(file_path):
    '''
    Returns the size of file in bytes. Returns zero on error.

    :param file_path: path to file
    :type file_path: str
    :return: int
    '''
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        logging.error('Could not get file size: {} {}'.format(sys.exc_info()[0].__name__, e))
        return 0


def get_file_size_without_padding(file_path):
    '''
    Returns the size of file in bytes minus size of padding areas.

    :param file_path: path to file
    :type file_path: str
    :return: int
    '''
    file_data = get_binary_from_file(file_path)
    return get_binary_size_without_padding(file_data)


def get_binary_size_without_padding(data, blocksize=BLOCKSIZE, padding_entropy_threshold=PADDING_ENTROPY_THRESHOLD):
    '''
    Returns the size of input_data in bytes minus size of padding areas.

    :param data: input data
    :type data: bytes
    :param blocksize: block-size regarding padding detection
    :type blocksize: int
    :param padding_entropy_threshold: shannon entropy threshold regarding padding detection
    :type padding_entropy_threshold: float
    :return: int
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
