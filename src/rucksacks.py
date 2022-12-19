from typing import List, Optional


def find_repeated_item_in(rucksacks: List[str]) -> Optional[str]:
    group_1 = rucksacks[0]
    group_2 = rucksacks[1]
    group_3 = rucksacks[2]

    common = find_common_between_two_list(group_1, group_2)
    result = find_common_between_two_list(common, group_3)

    return result[0] if len(result) == 1 else None


def find_common_between_two_list(group_1, group_2) -> List[str]:
    common = []
    for item in group_1:
        for item_2 in group_2:
            if item == item_2 and item not in common:
                common.append(item)

    return common


def calculate_total_item_priorities(rucksacks: List[str]) -> int:
    priorities = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                  "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
                  "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34,
                  "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45,
                  "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}

    total = 0
    elf_group = []
    for i, rucksack in enumerate(rucksacks):
        elf_group.append(rucksack)

        if (i + 1) % 3 == 0:
            repeated_item = find_repeated_item_in(elf_group)
            elf_group = []
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

