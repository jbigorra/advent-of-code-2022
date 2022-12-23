from typing import Tuple

import pytest

from src.camp_cleanup import find_overlapping_pairs_from, exist_within_range, pair_exist_within_range


# """
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# """

class TestNumberExistWithinRange:
    def test_number_exist_within_range(self):
        pair1 = (2, 8)

        result = exist_within_range(range_=pair1, number=3)

        assert result is True

    def test_number_does_not_exist_within_range(self):
        pair1 = (2, 8)

        result = exist_within_range(range_=pair1, number=1)

        assert result is False


class TestPairExistWithinARange:
    @pytest.mark.parametrize("pair_out_of_range", [
        (0, 1),
        (1, 2),
        (8, 12),
        (9, 12),
    ])
    def test_pair_does_not_exist_within_range_given_first_number_is_out_of_range(
        self, pair_out_of_range: Tuple[int, int]
    ):
        range_ = (2, 8)
        result = pair_exist_within_range(range_=range_, pair=pair_out_of_range)

        assert result is False

    def test_pair_exist_within_range(self):
        range = (2, 8)
        pair2 = (3, 7)

        result = pair_exist_within_range(range_=range, pair=pair2)

        assert result is True


class TestCampCleanup:
    def test_no_overlapping_pairs_found(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 0

    def test_find_one_overlapping_pair(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 1

    def test_find_two_overlapping_pairs(self):
        assert True is False
