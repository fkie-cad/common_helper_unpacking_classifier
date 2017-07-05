def _calculate_end_of_block(current_offset, block_size, max_size):
    result = current_offset + block_size
    if result > max_size:
        result = max_size
    return result
