class TennisGame:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.s1 = 0
        self.s2 = 0
        self.points = ["Love", "Fifteen", "Thirty", "Forty"]
        self.score = ""

    def won_point(self, player_name):
        if player_name == "player1":
            self.s1 = self.s1 + 1
        else:
            self.s2 = self.s2 + 1

    def even(self):
        if self.s1 != self.s2:
            return False
        if self.s1 >= 4 and self.s2 >= 4:
            self.score = "Deuce"
            return True
        self.score = self.points[self.s1] + "-All"
        return True

    def advantage(self):
        if self.s1 < 4 and self.s2 < 4:
            return False
        if self.s1 - self. s2 == 1:
            self.score = "Advantage player1"
            return True
        self.score = "Advantage player2"
        return True
        
    def win(self):
        if self.s1 >= 4 or self.s2 >= 4:
            minus_result = self.s1 - self.s2
            if minus_result > 1:
                self.score = "Win for player1"
                return True
            elif minus_result < -1:
                self.score = "Win for player2"
                return True
        return False

    def get_score(self):
        if self.win() or self.even() or self.advantage(): return self.score
        self.score = self.points[self.s1] + "-" + self.points[self.s2]
        return self.score
