import heapq
import os


class ScoreRow:
    def __init__(self, player_name, player_score):
        self.player_name = player_name
        self.player_score = int(player_score)

    def __str__(self):
        return f"{self.player_name} - {self.player_score}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.player_score < other.player_score


class HighscoreTable:
    def __init__(self, path="data/logic/highscores.txt"):
        self.path = path
        self.data = []
        self.n = 27
        self.load_from_file()
        self.update_drawer_data()


    def keep_n(self):
        self.data = heapq.nlargest(self.n, self.data)

    def load_from_file(self):
        if not os.path.isfile(self.path):
            open(self.path, 'a+').close()
        with open(self.path, encoding="utf-8", mode="r") as file:
            self.data = [ScoreRow(*line.strip().split(" - ")) for line in file if line.strip()]
            self.keep_n()
        self.update_drawer_data()

    def insert_to_file(self):
        with open(self.path, encoding="utf-8", mode="w") as file:
            for line in self.data:
                print(line, file=file)

    def add_score(self, player_name, player_score):
        self.data.append(ScoreRow(player_name, player_score))
        self.keep_n()
        self.update_drawer_data()

    def update_drawer_data(self):
        self.drawer_data = [{"name": row.player_name, "score": row.player_score} for row in self.data]

    def get_data(self):
        return self.drawer_data

    def __getitem__(self, item):
        if 0 <= item < len(self.data):
            return int(self.data[0].player_score)
        return "0"