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

        assert actual == [
            1000, 2000, 3000,
            0,
            4000,
            0,
            5000, 6000,
            0,
            7000, 8000, 9000,
            0,
            10000
        ]

    def test_highest_calorie_is_zero(self):
        calories = []

        actual = find_highest_calories_count(calories)

        assert actual == 0

    def test_find_highest_calories_count_from_one_elf(self):
        calories = [1000, 2000, 3000]

        actual = find_highest_calories_count(calories)

        assert actual == 6000

    def test_highest_calorie_count_is_from_first_and_second_elf(self):
        calories = [1000, 2000, 3000, 0, 1000]

        actual = find_highest_calories_count(calories)

        assert actual == 7000

    def test_highest_calorie_count_is_from_first_second_and_third_elf(self):
        calories = [1000, 2000, 3000, 0, 11000, 0, 10000]

        actual = find_highest_calories_count(calories)

        assert actual == 27000

    def test_highest_calorie_count_is_from_first_third_and_fourth(self):
        calories = [3000, 0, 1000, 0, 10000, 0, 12000]

        actual = find_highest_calories_count(calories)

        assert actual == 25000

    def test_find_highest_calories_count_from_multiple_elves(self):
        calories = parse_calories(ELVES_CALORIES_SAMPLE)

        actual = find_highest_calories_count(calories)

        assert actual == 45000

