from src.rucksacks import find_repeated_item_in


class TestRucksacks:
    def test_find_repeated_item(self):
        rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"

        item = find_repeated_item_in(rucksack)

        assert item == "p"

    def test_cannot_find_repeated_item(self):
        rucksack = "vJrwvWtwJgWrhcsFMMfFFhFp"

        item = find_repeated_item_in(rucksack)

        assert item is None
