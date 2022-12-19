def calculate_my_round_score(line: str) -> int:
    hands = line.split(" ")
    their_hand = hands[0]
    my_hand = hands[1]
    my_score = 0

    if my_hand == "X" and their_hand == "C":
        my_score = 7
    elif my_hand == "Y" and their_hand == "A":
        my_score = 8

    return my_score


def play_match() -> int:
    file = open("rock_paper_scissors_input.txt", "r")
    line = file.readline()
    my_score = 0

    while line:
        my_round_score = calculate_my_round_score(line)
        my_score += my_round_score
        line = file.readline()

    file.close()

    return my_score


def read_sample_file(filename) -> str:
    file = open(filename, "r")

    file_content = file.readline()

    file.close()

    print(file_content)

    return file_content


if __name__ == '__main__':
    result = play_match()
    print(result)
