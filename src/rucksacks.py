from typing import List, Optional


def find_repeated_item_in(rucksack: str) -> Optional[str]:
    middle_idx = int(len(rucksack) / 2)

    for i in range(0, middle_idx):
        for j in range(middle_idx, len(rucksack)):
            if rucksack[i] == rucksack[j]:
                return rucksack[i]


def calculate_total_item_priorities(rucksacks: List[str]) -> int:
    priorities = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                  "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
                  "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34,
                  "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45,
                  "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}

    total = 0
    for rucksack in rucksacks:
        repeated_item = find_repeated_item_in(rucksack)
        if repeated_item:
            total += priorities[repeated_item]

    return total


def parse_rucksacks(string: str) -> List[str]:
    return string.split("\n")


def read_sample_file(filename) -> str:
    file = open(filename, "r")

    file_content = file.read()

    file.close()

    return file_content


def run():
    file_string = read_sample_file("rucksacks_input.txt")

    rucksacks = parse_rucksacks(file_string)

    return calculate_total_item_priorities(rucksacks)


if __name__ == '__main__':
    result = run()

    print(result)

