# Unpacking Classifier
[![Build Status](https://travis-ci.org/fkie-cad/common_helper_unpacking_classifier.svg?branch=master)](https://travis-ci.org/fkie-cad/common_helper_unpacking_classifier)

Try to guess if unpacking was successfull.
Check if
 * Resulting data is uncompressed and unencrypted utilizing entropy
 * Data was uncompressed completly utilizing file sizes and padding detection
 
## Requirements

 * [entropy >= 0.9](https://pypi.python.org/pypi/entropy/0.9)
