import pytest

from src.camp_cleanup import find_overlapping_pairs_from, exist_within_range, pair_exist_within_range, parse_elf_pairs, \
    parse_one_elf, parse_one_pair_of_elves


class TestNumberExistWithinRange:
    def test_number_exist_within_range(self):
        pair1 = (2, 8)

        result = exist_within_range(range_=pair1, number=3)

        assert result is True

    def test_number_does_not_exist_within_range(self):
        pair1 = (2, 8)

        result = exist_within_range(range_=pair1, number=1)

        assert result is False


class TestPairsOverlaps:
    @pytest.mark.parametrize("pair_out_of_range", [
        (0, 1),
        (9, 12),
    ])
    def test_pair_does_not_exist_within_range_given_first_number_is_out_of_range(
            self, pair_out_of_range: tuple[int, int]
    ):
        range_ = (2, 8)
        result = pair_exist_within_range(range_=range_, pair=pair_out_of_range)

        assert result is False

    @pytest.mark.parametrize("pair", [
        ((1, 2)),
        ((8, 9)),
        ((3, 7))
    ])
    def test_pair_exist_within_range(self, pair: tuple[int, int]):
        range_ = (2, 8)

        result = pair_exist_within_range(range_=range_, pair=pair)

        assert result is True


class TestFindOverlappingPairs:
    def test_no_overlapping_pairs_found(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 0

    def test_one_right_pair_is_contained_within_left_pair(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 1

    def test_two_right_pairs_are_contained_within_two_left_pairs(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
            ((4, 6), (6, 6)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 2

    def test_one_left_pair_is_contained_within_right_pair(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((3, 7), (2, 8)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 1

    def test_two_left_pairs_are_contained_within_two_right_pairs(self):
        pairs = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((3, 7), (2, 8)),
            ((6, 6), (4, 6)),
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 2

    def test_multiple_pairs_left_and_right_contained_within_each_other(self):
        pairs = (
            ((3, 4), (3, 5)),  # contained
            ((2, 4), (4, 5)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((3, 7), (2, 8)),  # contained
            ((6, 6), (4, 6)),  # contained
        )

        result = find_overlapping_pairs_from(pairs)

        assert result == 3


class TestParseOneElfPair:
    def test_parse_one_elf(self):
        string = "2-4"

        pairs = parse_one_elf(string)

        assert pairs == (2, 4)

    @pytest.mark.parametrize("string", [
        "",
        "invalid-string",
        "invalid",
        "invalid-"
        "1-",
        "-2"
    ])
    def test_parse_one_elf_raises_exception(self, string: str):
        with pytest.raises(Exception,  match=f"Wrong format"):
            parse_one_elf(string)


class TestParseTwoElvesPairs:
    def test_parse_two_elves(self):
        string = "2-4,6-8"

        pair_of_elves = parse_one_pair_of_elves(string)

        assert pair_of_elves == ((2, 4), (6, 8))

    @pytest.mark.parametrize("string", [
        "",
        ",",
        "2-4",
        "2-4,",
        ",6-8",
        "1,",
        ",2"
    ])
    def test_parse_one_elf_raises_exception(self, string: str):
        with pytest.raises(Exception, match=f"Wrong format"):
            parse_one_pair_of_elves(string)


class TestParseListOfElvesPairs:
    FILE_SAMPLE = """2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8"""

    def test_parse_elf_pairs(self):

        result = parse_elf_pairs(self.FILE_SAMPLE)

        expected = (
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
            ((6, 6), (4, 6)),
            ((2, 6), (4, 8)),
        )

        assert result == expected

    def test_raise_exception(self):
        file_input = ""
        with pytest.raises(Exception, match="Wrong input file format"):
            parse_elf_pairs("")
