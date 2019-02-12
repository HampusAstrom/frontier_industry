import random as rng

class Area:

    def __init__(self):
        self.tot_area = 1
        self.fertile = rng.uniform(0, 1)
        rest = 1 - self.fertile
        self.grazeable = rng.uniform(0, rest)
        self.barren = rest - self.grazeable

        self.fert_forest = rng.uniform(self.fertile/2, self.fertile)
        self.graze_forest = rng.uniform(self.grazeable/4, self.grazeable)

    def get_forest(self):
        return self.fert_forest + self.graze_forest
