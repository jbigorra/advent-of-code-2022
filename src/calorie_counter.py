from typing import List


def parse_calories(elves_calories: str) -> List[int]:
    calories = list(
        map(
            lambda val: int(val) if val != "" else 0,
            elves_calories.split("\n")
        )
    )

    return calories


def find_highest_calories_count(calories: List[int]) -> int:
    highest_count = 0
    counter = 0

    for i, calorie in enumerate(calories):
        counter += calorie

        if calorie == 0 or i == (len(calories) - 1):
            if counter >= highest_count:
                highest_count = counter

            counter = 0

    return highest_count
