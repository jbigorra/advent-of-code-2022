# Rock      A and X - 1
# Paper     B and Y - 2
# Scissors  C and Z - 3
# Lose = 0, draw = 3, win = 6
from src.rock_paper_scissors import calculate_my_round_score


class TestRockPaperScissorScoring:
    def test_i_win_with_rock_over_scissors(self):
        line = "C X"

        my_score = calculate_my_round_score(line)

        assert my_score == 7

    def test_i_win_with_paper_over_rock(self):
        line = "A Y"

        my_score = calculate_my_round_score(line)

        assert my_score == 8

    def test_i_win_with_scissors_over_paper(self):
        line = "B Z"

        my_score = calculate_my_round_score(line)

        assert my_score == 9

    def test_i_lose_with_rock_over_scissors(self):
        line = "A Z"

        my_score = calculate_my_round_score(line)

        assert my_score == 3

    def test_i_lose_with_paper_over_rock(self):
        line = "B X"

        my_score = calculate_my_round_score(line)

        assert my_score == 1

    def test_i_lose_with_scissors_over_paper(self):
        line = "C Y"

        my_score = calculate_my_round_score(line)

        assert my_score == 2

    def test_i_draw_with_rock(self):
        line = "A X"

        my_score = calculate_my_round_score(line)

        assert my_score == 4

    def test_i_draw_with_paper(self):
        line = "B Y"

        my_score = calculate_my_round_score(line)

        assert my_score == 5

    def test_i_draw_with_scissors(self):
        line = "C Z"

        my_score = calculate_my_round_score(line)

        assert my_score == 6


