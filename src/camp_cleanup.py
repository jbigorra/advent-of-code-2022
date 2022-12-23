from typing import Tuple


def find_overlapping_pairs_from(pairs):
    for set_of_pairs in pairs:
        pair_1 = set_of_pairs[0]
        pair_2 = set_of_pairs[1]
        print(pair_1, pair_2)
        if pair_1[0] < pair_2[0] < pair_1[1]:
            return 1

    return 0