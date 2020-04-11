
class TennisGame:
    def __init__(self):
        self._p1_score = 0
        self._p2_score = 0

    @property
    def score(self):
        return self._calculate_score()

    def player_one_scored(self):
        self._p1_score += 1

    def player_two_scored(self):
        self._p2_score += 1

    def _calculate_score(self) -> str:
        if self._is_winner():
            return f"Game for {self._player_with_highest_score()}"
        if self._is_deuce():
            return "Deuce"
        if self._is_advantage():
            return f"Advantage {self._player_with_highest_score()}"
        if self._p1_score == self._p2_score:
            return f"{self._translate_score(self._p1_score)} all"
        return "{} {}".format(
            self._translate_score(self._p1_score),
            self._translate_score(self._p2_score)
        )

    def _is_winner(self):
        return (self._p1_score >= 4 or self._p2_score >= 4) \
               and abs(self._p1_score - self._p2_score) >= 2

    def _is_deuce(self):
        return self._p1_score >= 4 and \
               self._p2_score >= 4 and \
               self._p1_score == self._p2_score

    def _is_advantage(self):
        return self._p1_score >= 4 and \
               self._p2_score >= 4 and \
               abs(self._p1_score - self._p2_score) == 1

    def _player_with_highest_score(self):
        if self._p1_score > self._p2_score:
            return "P1"
        return "P2"

    def _translate_score(self, player_score):
        if player_score == 0:
            return "Love"
        elif player_score == 1:
            return "Fifteen"
        elif player_score == 2:
            return "Thirty"
        elif player_score == 3:
            return "Forty"
