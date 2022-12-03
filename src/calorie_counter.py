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
    calories_counter = 0

    for calorie in calories:
        calories_counter += calorie

    return calories_counter
