def exist_within_range(range_: tuple[int, int], number: int) -> bool:
    return True if range_[0] <= number <= range_[1] else False


def pair_exist_within_range(range_: tuple[int, int], pair: tuple[int, int]) -> bool:
    if exist_within_range(range_=range_, number=pair[0]) or exist_within_range(range_=range_, number=pair[1]):
        return True

    return False


def find_overlapping_pairs_from(pairs):
    overlaps = 0
    for [left_pair, right_pair] in pairs:
        if (
            pair_exist_within_range(range_=left_pair, pair=right_pair) or
            pair_exist_within_range(range_=right_pair, pair=left_pair)
        ):
            overlaps += 1

    return overlaps


def parse_one_elf(string: str) -> tuple[int, ...]:
    try:
        pair = tuple(map(lambda n: int(n), string.split("-")))
    except Exception:
        raise Exception(f"Wrong format")

    return pair


def parse_one_pair_of_elves(string: str) -> tuple[tuple[int, ...], ...]:
    pair_of_elves_str = string.split(",")

    if len(pair_of_elves_str) <= 1:
        raise Exception(f"Wrong format")

    one_pair_of_elves = tuple(
        map(lambda elf: parse_one_elf(elf), pair_of_elves_str)
    )

    return one_pair_of_elves


def parse_elf_pairs(file_string: str):
    if not file_string:
        raise Exception("Wrong input file format")

    lines = file_string.split("\n")

    return tuple(
        map(
            lambda line: parse_one_pair_of_elves(line),
            lines
        )
    )


def read_sample_file(filename) -> str:
    file = open(filename, "r")

    file_content = file.read()

    file.close()

    return file_content


def run_camp_cleanup():
    file_string = read_sample_file("camp_cleanup_input.txt")

    elf_pairs = parse_elf_pairs(file_string)

    return find_overlapping_pairs_from(elf_pairs)


if __name__ == '__main__':
    result = run_camp_cleanup()
    print(result)
