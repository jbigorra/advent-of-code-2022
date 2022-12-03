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
    highest_count = [0, 0, 0]
    counter = 0

    for i, calorie in enumerate(calories):
        counter += calorie

        if calorie == 0 or i == (len(calories) - 1):
            if counter >= highest_count[0]:
                highest_count[2] = highest_count[1]
                highest_count[1] = highest_count[0]
                highest_count[0] = counter
            elif counter >= highest_count[1]:
                highest_count[2] = highest_count[1]
                highest_count[1] = counter
            elif counter >= highest_count[2]:
                highest_count[2] = counter

            counter = 0

    return sum(highest_count)


def read_sample_file(filename) -> str:
    file = open(filename, "r")

    file_content = file.read()

    file.close()

    print(file_content)

    return file_content


def calculate_highest_calories_count():
    file_string = read_sample_file("elves_calories.txt")

    calories = parse_calories(file_string)

    return find_highest_calories_count(calories)


if __name__ == '__main__':
    result = calculate_highest_calories_count()
    print(result)
