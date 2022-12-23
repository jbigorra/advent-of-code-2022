from src.camp_cleanup import find_overlapping_pairs_from

# """
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
# """

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
