class LifeCounter:
    def __init__(self):
        self.life = 3

    def add(self):
        self.life += 1

    def remove(self):
        self.life -= 1
        if self.life < 0:
            raise RuntimeError
