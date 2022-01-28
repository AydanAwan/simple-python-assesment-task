"""class and metheod for calculating the standard devieation."""


class meanDeviation:

    def __init__(self, mean, length, dataset):
        self.mean = mean
        self.length = length
        self.data = dataset

    def calMeanDev(self):
        y = 0
        for x in self.data:
            y += abs(x - self.mean)
        return y / (self.length)
