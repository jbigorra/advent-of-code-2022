from src.camp_cleanup import find_overlapping_pairs_from


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
        assert True is False

    def test_find_two_overlapping_pairs(self):
        assert True is False
