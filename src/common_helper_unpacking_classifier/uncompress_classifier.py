import logging
from typing import Callable

from entropython import metric_entropy as entropy

SMALL_SIZE_THRESHOLD = 255
VERY_SMALL_SIZE_THRESHOLD = 50
COMPRESS_ENTROPY_THRESHOLD = 0.8
COMPRESS_ENTROPY_THRESHOLD_SMALL_FILE = 0.65


def is_compressed(
    raw_data: bytes,
    small_size_threshold: int = SMALL_SIZE_THRESHOLD,
    compress_entropy_threshold: float = COMPRESS_ENTROPY_THRESHOLD,
    very_small_size_threshold: int = VERY_SMALL_SIZE_THRESHOLD,
    compress_entropy_threshold_small_file: float = COMPRESS_ENTROPY_THRESHOLD_SMALL_FILE,
    classifier: Callable = entropy
) -> bool:
    '''
    Try to guess if the input data is compressed.

    :param raw_data: input data
    :param small_size_threshold: input smaller than this size is classified using compress_entropy_threshold_small_file
    :param compress_entropy_threshold: if input data's entropy is above this threshold, the data is considered packed
    :param very_small_size_threshold: if input data's size is smaller this threshold result is undecidable
    :param compress_entropy_threshold_small_file: like compress_entropy_threshold but for input data smaller than
        small_size_threshold
    :param classifier: entropy function to use
    :return: True if `raw_data` seems to be compressed and False otherwise
    '''
    if len(raw_data) > small_size_threshold:
        return classifier(raw_data) > compress_entropy_threshold
    if len(raw_data) > very_small_size_threshold:
        logging.debug('compression classification might be wrong: file is small')
        return is_compressed(
            raw_data, small_size_threshold=very_small_size_threshold,
            compress_entropy_threshold=compress_entropy_threshold_small_file, classifier=classifier
        )
    logging.debug('could not determine compression: file too small')
    return False
