class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, name):
        if name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if (self.player1_points < 4 and self.player2_points < 4) and (self.player1_points + self.player2_name < 6):
            score_names = ["Love", "Fifteen", "Thirty", "Forty"]
            score = score_names[self.player1_points]
            return score + "-All" if (self.player1_points == self.player2_points) else s + "-" + score_names[self.player2_points]
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"
            s = self.player1_name if self.player1_points > self.player2_points else self.player1_points
            return (
                "Advantage " + s
                if ((self.play - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + s
            )
