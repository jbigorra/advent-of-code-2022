import re


class Stack:
    def __init__(self, items: list[str]):
        self._items = items

    def pop(self) -> str:
        return self._items.pop()

    def append(self, item: str) -> None:
        self._items.append(item)

    def last(self) -> any:
        return self._items[len(self._items) - 1]


class CargoCrane:
    def __init__(self, stacks: list[Stack], moves: list[tuple[int, ...]]):
        self._moves = moves
        self._stacks = stacks

    pass

    def arrange_stacks(self) -> str:
        for move in self._moves:
            self._move(number=move[0], _from=move[1], _to=move[2])

        return "".join([stack.last() for stack in stacks])

    def _move(self, number: int, _from: int, _to: int) -> None:
        for i in range(0, number):
            item = self._stacks[_from - 1].pop()
            self._stacks[_to - 1].append(item)


def parse_stacks_from(lines: list[str]) -> list[Stack]:
    return [
        Stack(["S", "C", "V", "N"]),
        Stack(["Z", "M", "J", "H", "N", "S"]),
        Stack(["M", "C", "T", "G", "J", "N", "D"]),
        Stack(["T", "D", "F", "J", "W", "R", "M"]),
        Stack(["P", "F", "H"]),
        Stack(["C", "T", "Z", "H", "J"]),
        Stack(["D", "P", "R", "Q", "F", "S", "L", "Z"]),
        Stack(["C", "S", "L", "H", "D", "F", "P", "W"]),
        Stack(["D", "S", "M", "P", "F", "N", "G", "Z"])
    ]


def parse_item_moves(lines: list[str]) -> list[tuple[int, ...]]:
    item_moves = []
    for i in range(10, len(lines)):
        line = lines[i]

        match = tuple(
            map(lambda x: int(x), re.findall(r"\d+", line))
        )

        item_moves.append(match)

    return item_moves


def read_sample_file(filename) -> str:
    file = open(filename, "r")

    file_content = file.read()

    file.close()

    return file_content


if __name__ == "__main__":
    input_string = read_sample_file("supply_stack_input.txt")
    lines = input_string.split("\n")
    stacks = parse_stacks_from(lines)
    moves = parse_item_moves(lines)

    cargo_crane = CargoCrane(stacks, moves)

    print(cargo_crane.arrange_stacks())
