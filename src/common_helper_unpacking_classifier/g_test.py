import logging
import sys
from math import log


def g_test(frequencies):
    elements = sum(frequencies)
    g = 0
    for frequency in frequencies:
        if frequency > 0:
            try:
                g += frequency * log(frequency / (elements / 256))
            except Exception as e:
                logging.error('Could not calculate g_test element: {} {}'.format(sys.exc_info()[0].__name__, e))
        else:
            g += frequency
    return 2 * g
