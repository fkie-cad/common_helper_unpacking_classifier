from collections import Counter
from math import log


def shannon_entropy_byte(data):
    '''
    Returns the byte entropy of data
    :param data: input data
    :type data: bytes
    :return: float
    '''
    probabilities = [count / len(data) for count in Counter(data).values()]
    entropy = sum(prob * log(prob, 2) for prob in probabilities)
    return -entropy


def normalized_shannon_byte_entropy(data):
    return shannon_entropy_byte(data) / log(256, 2)
