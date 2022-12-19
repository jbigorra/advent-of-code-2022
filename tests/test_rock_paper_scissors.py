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
        pass

    def test_i_lose_with_rock_over_scissors(self):
        pass

    def test_i_lose_with_paper_over_rock(self):
        pass

    def test_i_lose_with_scissors_over_paper(self):
        pass

    def test_i_draw_with_rock(self):
        pass

    def test_i_draw_with_scissors(self):
        pass

    def test_i_draw_with_paper(self):
        pass


