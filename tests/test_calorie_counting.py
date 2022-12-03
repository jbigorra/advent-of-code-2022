from src.calorie_counter import parse_calories

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
