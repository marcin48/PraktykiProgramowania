class TennisGame2:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def even_score(self):
        if self.player1_points < 3:
            return f"{self.point_name(self.player1_points)}-All"
        return "Deuce"

    def end_game_score(self):
        diff = self.player1_points - self.player2_points
        if diff == 1:
            return f"Advantage {self.player1_name}"
        elif diff == -1:
            return f"Advantage {self.player2_name}"
        elif diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def score(self):
        if self.player1_points == self.player2_points:
            return self.even_score()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            return self.end_game_score()
        else:
            return f"{self.point_name(self.player1_points)}-{self.point_name(self.player2_points)}"

        # ---------------------------------------------------------------

    def point_name(self, point):
        return self.SCORE_NAMES[point]

    def set_p1_score(self, number):
        self.player1_points = number

    def set_p2_score(self, number):
        self.player2_points = number
