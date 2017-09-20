from collections import Counter
from math import log


def shannon_entropy_byte(data):
    '''
    Returns the byte entropy of data
    :param data: input data
    :type data: bytes
    :return: float
    '''
    probabilities = (count / len(data) for count in Counter(data).values())
    entropy = 0
    for prob in probabilities:
        entropy += prob * log(prob, 2)

    return -entropy
