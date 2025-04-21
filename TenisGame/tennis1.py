class TennisGame1:
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
        score_names = ["Love-All", "Fifteen-All", "Thirty-All"]
        return score_names[self.player1_points] if self.player1_points < 3 else "Deuce"

    def end_game_score(self):
        score_diff = self.player1_points - self.player2_points
        if score_diff == 1:
            return "Advantage player1"
        elif score_diff == -1:
            return "Advantage player2"
        elif score_diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def regular_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.player1_points]}-{score_names[self.player2_points]}"

    def score(self):
        if self.player1_points == self.player2_points:
            return self.even_score()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            return self.end_game_score()
        else:
            return self.regular_score()
