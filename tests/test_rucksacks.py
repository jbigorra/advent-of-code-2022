from src.rucksacks import find_repeated_item_in


class TestRucksacks:
    def test_find_repeated_item(self):
        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg"
        ]

        item = find_repeated_item_in(rucksacks)

        assert item == "r"

    def test_cannot_find_repeated_item(self):
        rucksacks = [
            "AAAA",
            "BBBBBB",
            "CC"
        ]

        item = find_repeated_item_in(rucksacks)

        assert item is None
