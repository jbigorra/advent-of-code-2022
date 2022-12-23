from typing import Tuple


def exist_within_range(range_: Tuple[int, int], number: int) -> bool:
    return True if range_[0] <= number <= range_[1] else False


def pair_exist_within_range(range_: Tuple[int, int], pair: Tuple[int, int]) -> bool:
    if exist_within_range(range_=range_, number=pair[0]) and exist_within_range(range_=range_, number=pair[1]):
        return True

    return False


def find_overlapping_pairs_from(pairs):
    overlaps = 0
    for [left_pair, right_pair] in pairs:
        print(left_pair, right_pair)
        if (
            pair_exist_within_range(range_=left_pair, pair=right_pair) or
            pair_exist_within_range(range_=right_pair, pair=left_pair)
        ):
            overlaps += 1

    return overlaps


def parse_one_elf(string: str):
    try:
        pair = tuple(map(lambda n: int(n), string.split("-")))
    except Exception:
        raise Exception(f"Invalid elf pair. Wrong format: {string}")

    return pair
