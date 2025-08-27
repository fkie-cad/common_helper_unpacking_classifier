from __future__ import annotations

from io import BufferedReader
from pathlib import Path
from typing import Iterable


def iter_content_in_chunks(
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
