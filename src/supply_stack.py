#                         [Z] [W] [Z]
#         [D] [M]         [L] [P] [G]
#     [S] [N] [R]         [S] [F] [N]
#     [N] [J] [W]     [J] [F] [D] [F]
# [N] [H] [G] [J]     [H] [Q] [H] [P]
# [V] [J] [T] [F] [H] [Z] [R] [L] [M]
# [C] [M] [C] [D] [F] [T] [P] [S] [S]
# [S] [Z] [M] [T] [P] [C] [D] [C] [D]
#  1   2   3   4   5   6   7   8   9
from typing import Generic


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
    def __init__(self, stacks: list[Stack], moves: list[tuple[int, int, int]]):
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


def parse_stacks_from(input_string: str) -> list[Stack]:
    #     [D]
    # [Z] [C]
    # [N] [M] [P]
    # 1   2   3
    return [
        Stack(["Z", "N"]),
        Stack(["M", "C", "D"]),
        Stack(["P"]),
    ]


def parse_item_moves(input_string: str) -> list[tuple[int, int, int]]:
    # move 1 from 2 to 1
    # move 3 from 1 to 3
    # move 2 from 2 to 1
    # move 1 from 1 to 2

    return [
        (1, 2, 1),
        (3, 1, 3),
        (2, 2, 1),
        (1, 1, 2),
    ]


if __name__ == "__main__":
    input_string = ""
    stacks = parse_stacks_from(input_string)
    moves = parse_item_moves(input_string)

    cargo_crane = CargoCrane(stacks, moves)

    print(cargo_crane.arrange_stacks())
