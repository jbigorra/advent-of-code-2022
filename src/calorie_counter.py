from typing import List


def parse_calories(elves_calories: str) -> List[int]:
    calories = list(
        map(
            lambda val: int(val) if val != "" else 0,
            elves_calories.split("\n")
        )
    )

    return calories
