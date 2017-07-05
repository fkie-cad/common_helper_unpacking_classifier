from entropy import shannon_entropy
import logging

SMALL_SIZE_THRESHOLD = 255
VERY_SMALL_SIZE_THRESHOLD = 50
COMPRESS_ENTROPY_THRESHOLD = 0.8
COMPRESS_ENTROPY_THRESHOLD_SMALL_FILE = 0.65


def is_compressed(raw_data, small_size_threshold=SMALL_SIZE_THRESHOLD, compress_entropy_threshold=COMPRESS_ENTROPY_THRESHOLD, very_small_size_threshold=VERY_SMALL_SIZE_THRESHOLD, compress_entropy_threshold_small_file=COMPRESS_ENTROPY_THRESHOLD_SMALL_FILE, classifier=shannon_entropy):
    """
    Try to guess if data is compressed

    :param raw_data: input data
    :type raw_data: bytes
    :param small_size_threshold: data smaller this size are classified using compress_entropy_threshold_small_file
    :type small_size_threshold: int
    :param compress_entropy_threshold: input data's entropy is above this threshold the data is considered packed
    :type compress_entropy_threshold: float
    :param very_small_size_threshold: if input data's size is smaller this threshold result is un-decideable
    :type very_small_size_threshold: int
    :param compress_entropy_threshold_small_file: like compress_entropy_threshold but for input data smaller small_size_threshold
    :type compress_entropy_threshold_small_file: float
    :param classifier: entropy function to use
    :type: <function>
    :return: bool
    """
    if len(raw_data) > small_size_threshold:
        if classifier(raw_data) > compress_entropy_threshold:
            return True
        else:
            return False
    elif len(raw_data) > very_small_size_threshold:
        logging.warning("compression classification might be wrong: file is small")
        return is_compressed(raw_data, small_size_threshold=very_small_size_threshold, compress_entropy_threshold=compress_entropy_threshold_small_file, classifier=classifier)
    else:
        logging.warning("could not determine compression: file too small")
        return False
