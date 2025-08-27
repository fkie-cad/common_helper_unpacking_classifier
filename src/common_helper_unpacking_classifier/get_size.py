from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

from entropython import metric_entropy as entropy

from .utils import iter_content_in_chunks

BLOCKSIZE = 256
PADDING_ENTROPY_THRESHOLD = 0.1


def get_file_size(file_path: str | Path) -> int:
    logging.warning(
        "Deprecation warning: this function is no longer supported. "
        "Please use pathlib.Path.stat().st_size instead."
    )
    return Path(file_path).stat().st_size


def get_file_size_without_padding(
    file_path: str | Path,
    blocksize: int = BLOCKSIZE,
    padding_entropy_threshold: float = PADDING_ENTROPY_THRESHOLD,
) -> int:
    """
    Returns the size of file in bytes minus size of padding areas.

    :param file_path: path to file
    :param blocksize: block-size regarding padding detection
    :param padding_entropy_threshold: shannon entropy threshold regarding padding detection
    :return: int
    """
    file_size = Path(file_path).stat().st_size
    return _get_size_without_padding(
        iter_content_in_chunks(file_path, blocksize),
        file_size,
        padding_entropy_threshold,
    )


def get_binary_size_without_padding(
    data: bytes,
    blocksize: int = BLOCKSIZE,
    padding_entropy_threshold: float = PADDING_ENTROPY_THRESHOLD,
) -> int:
    """
    Returns the size of input_data in bytes minus size of padding areas.

    :param data: input data
    :param blocksize: block-size regarding padding detection
    :param padding_entropy_threshold: shannon entropy threshold regarding padding detection
    :return: the size of input_data without padding
    """
    return _get_size_without_padding(
        iter_content_in_chunks(data, blocksize), len(data), padding_entropy_threshold
    )


def _get_size_without_padding(
    blocks: Iterable[bytes],
    original_size: int,
    entropy_threshold: float = PADDING_ENTROPY_THRESHOLD,
) -> int:
    padding_size = 0
    for block in blocks:
        if entropy(block) <= entropy_threshold:
            padding_size += len(block)
    return original_size - padding_size
