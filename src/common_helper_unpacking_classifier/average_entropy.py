from __future__ import annotations

import logging
from io import BufferedReader
from pathlib import Path
from typing import Callable, Iterable

from entropython import metric_entropy, shannon_entropy

BLOCKSIZE = 4096


def avg_entropy(
    input_data: bytes | Path | BufferedReader,
    block_size: int = BLOCKSIZE,
    entropy_function: Callable = metric_entropy,
) -> float:
    """
    Calculates the average entropy of input_data regarding block_size

    :param input_data: input data
    :param block_size: shannon block size in bytes
    :param entropy_function: the function to use for entropy calculation
    :return: float
    """
    entropy_sum = 0
    number_of_blocks = 0
    for block in _iter_content_in_chunks(input_data, block_size):
        block_weight = len(block) / block_size
        entropy_sum += entropy_function(block) * block_weight
        number_of_blocks += block_weight
    try:
        return entropy_sum / number_of_blocks
    except ZeroDivisionError:
        return 0.0
    except Exception as err:
        logging.exception(f"Could not calculate entropy: {err}")
        return 0.0


def _iter_content_in_chunks(
    input_data: Path | bytes | BufferedReader,
    chunk_size: int,
) -> Iterable[bytes]:
    if isinstance(input_data, Path):
        with input_data.open("rb") as fp:
            while chunk := fp.read(chunk_size):
                yield chunk
    elif isinstance(input_data, BufferedReader):
        while chunk := input_data.read(chunk_size):
            yield chunk
    else:
        for offset in range(0, len(input_data), chunk_size):
            yield input_data[offset : offset + chunk_size]


def avg_shannon_entropy(
    input_data: bytes | Path | BufferedReader,
    block_size: int = BLOCKSIZE,
) -> float:
    return avg_entropy(
        input_data,
        block_size=block_size,
        entropy_function=metric_entropy,
    )


def avg_shannon_entropy_byte(
    input_data: bytes | Path | BufferedReader,
    block_size: int = BLOCKSIZE,
) -> float:
    return avg_entropy(
        input_data,
        block_size=block_size,
        entropy_function=shannon_entropy,
    )
