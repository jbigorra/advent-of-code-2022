from src.calorie_counter import parse_calories, find_highest_calories_count

ELVES_CALORIES_SAMPLE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


class TestCalorieCounter:
    def test_parse_elves_calories_to_list(self):
        actual = parse_calories(ELVES_CALORIES_SAMPLE)

        assert [
            1000, 2000, 3000,
            0,
            4000,
            0,
            5000, 6000,
            0,
            7000, 8000, 9000,
            0,
            10000
        ] == actual

    def test_count_calories_from_one_elf(self):
        calories = [1000, 2000, 3000]

        actual = find_highest_calories_count(calories)

        assert 6000 == actual

    # def test_find_highest_calories_count(self):
    #     calories = parse_calories(ELVES_CALORIES_SAMPLE)
    #
    #     actual = find_highest_calories_count(calories)
    #
    #     assert 24000 == actual

