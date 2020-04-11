import unittest

from tennis_game import TennisGame


class TestTennisGame(unittest.TestCase):

    def setUp(self):
        self.game = TennisGame()

    def test_initial_score(self):
        initial_score = self.game.score
        self.assertEqual("Love all", initial_score)

    def test_score_is_15_0_when_p1_scored_once(self):
        self._create_score(1, 0)
        self.assertEqual("Fifteen Love", self.game.score)

    def test_score_is_15_15_when_both_scored_once(self):
        self._create_score(1, 1)
        self.assertEqual("Fifteen all", self.game.score)

    def test_score_is_30_0_when_p1_scored_twice(self):
        self._create_score(2, 0)
        self.assertEqual("Thirty Love", self.game.score)

    def test_score_is_30_15_when_p1_scored_twice_and_p2_scored_once(self):
        self._create_score(2, 1)
        self.assertEqual("Thirty Fifteen", self.game.score)

    def test_score_is_40_15_when_p1_scored_three_times_and_p2_scored_once(self):
        self._create_score(3, 1)
        self.assertEqual("Forty Fifteen", self.game.score)

    def test_score_is_15_30_when_p1_scored_once_and_p2_scored_twice(self):
        self._create_score(1, 2)
        self.assertEqual("Fifteen Thirty", self.game.score)

    def test_score_is_0_15_when_p2_scored_once(self):
        self._create_score(0, 1)
        self.assertEqual("Love Fifteen", self.game.score)

    def test_score_is_0_30_when_p2_scored_twice(self):
        self._create_score(0, 2)
        self.assertEqual("Love Thirty", self.game.score)

    def test_score_is_0_40_when_p2_scored_three_times(self):
        self._create_score(0, 3)
        self.assertEqual("Love Forty", self.game.score)

    def test_game_for_p1_when_scored_four_times(self):
        self._create_score(4, 0)
        self.assertEqual("Game for P1", self.game.score)

    def test_game_for_p2_when_scored_four_times(self):
        self._create_score(0, 4)
        self.assertEqual("Game for P2", self.game.score)

    def test_deuce(self):
        self._create_score(4, 4)
        self.assertEqual("Deuce", self.game.score)

    def test_deuce_when_both_scored_seven_times(self):
        self._create_score(7, 7)
        self.assertEqual("Deuce", self.game.score)

    def test_advantage_p1_when_score_5_4(self):
        self._create_score(5, 4)
        self.assertEqual("Advantage P1", self.game.score)

    def test_advantage_p1_when_score_12_11(self):
        self._create_score(12, 11)
        self.assertEqual("Advantage P1", self.game.score)

    def test_advantage_p2_when_score_4_5(self):
        self._create_score(4, 5)
        self.assertEqual("Advantage P2", self.game.score)

    def test_advantage_p1_when_score_11_12(self):
        self._create_score(11, 12)
        self.assertEqual("Advantage P2", self.game.score)

    def test_game_for_p1_after_deuce(self):
        self._create_score(6, 4)
        self.assertEqual("Game for P1", self.game.score)

    def test_game_for_p2_after_deuce(self):
        self._create_score(4, 6)
        self.assertEqual("Game for P2", self.game.score)

    def test_game_for_p1_when_score_24_22(self):
        self._create_score(24, 22)
        self.assertEqual("Game for P1", self.game.score)

    def _create_score(self, player_one_score, player_two_score):
        for _ in range(player_one_score):
            self.game.player_one_scored()
        for _ in range(player_two_score):
            self.game.player_two_scored()
