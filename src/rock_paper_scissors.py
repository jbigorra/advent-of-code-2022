def calculate_my_round_score(line: str) -> int:
    round = line.split(" ")
    their_hand = round[0]
    round_result = round[1]
    my_score = 0
    my_hand = ""

    if round_result == "Z":
        my_score += 6
        my_hand = _map_hand_to_win(their_hand)
    elif round_result == "X":
        my_hand = _map_hand_to_lose(their_hand)
    elif round_result == "Y":
        my_score += 3
        my_hand = _map_hand_to_draw(their_hand)

    if my_hand == "Rock":
        my_score += 1
    elif my_hand == "Paper":
        my_score += 2
    elif my_hand == "Scissor":
        my_score += 3

    return my_score


def _map_hand_to_draw(their_hand) -> str:
    if their_hand == "C":
        my_hand = "Scissor"
    elif their_hand == "B":
        my_hand = "Paper"
    elif their_hand == "A":
        my_hand = "Rock"
    return my_hand


def _map_hand_to_lose(their_hand) -> str:
    if their_hand == "C":
        my_hand = "Paper"
    elif their_hand == "B":
        my_hand = "Rock"
    elif their_hand == "A":
        my_hand = "Scissor"
    return my_hand


def _map_hand_to_win(their_hand) -> str:
    if their_hand == "C":
        my_hand = "Rock"
    elif their_hand == "B":
        my_hand = "Scissor"
    elif their_hand == "A":
        my_hand = "Paper"
    return my_hand


def play_match() -> int:
    file = open("rock_paper_scissors_input.txt", "r")
    line = file.readline()
    my_score = 0

    while line:
        my_round_score = calculate_my_round_score(line.strip("\n"))
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
