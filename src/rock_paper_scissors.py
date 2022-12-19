# Rock      A and X - 1
# Paper     B and Y - 2
# Scissors  c and Z - 3
# Lose = 0, draw = 3, win = 6

def calculate_my_round_score(line: str) -> int:
    pass


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
