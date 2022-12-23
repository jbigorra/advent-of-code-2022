from typing import Tuple


def exist_within_range(range_: Tuple[int, int], number: int) -> bool:
    return True if range_[0] <= number <= range_[1] else False


def pair_exist_within_range(range_: Tuple[int, int], pair: Tuple[int, int]) -> bool:
    if exist_within_range(range_=range_, number=pair[0]) and exist_within_range(range_=range_, number=pair[1]):
        return True

    return False

def find_overlapping_pairs_from(pairs):
    for set_of_pairs in pairs:
        pair_1 = set_of_pairs[0]
        pair_2 = set_of_pairs[1]
        print(pair_1, pair_2)
        if pair_1[0] < pair_2[0] < pair_1[1]:
            return 1

    return 0
