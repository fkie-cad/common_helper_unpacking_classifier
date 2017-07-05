import logging
import sys


def chi_square_test(frequencies):
    elements = sum(frequencies)
    chi = 0
    for frequency in frequencies:
        try:
            chi += (((elements / 256) - frequency) ** 2) / (elements / 256)
        except Exception as e:
            logging.error("Could not calculate chi_square element: {} {}".format(sys.exc_info()[0].__name__, e))

    return chi
