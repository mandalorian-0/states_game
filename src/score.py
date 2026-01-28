class Score:
    def __init__(self):
        self.score = 0

    def show_score(self):
        return self.score

    def increase_score(self):
        self.score += 1

    def has_guessed_all(self):
        return self.score <= 50