"""classs and method for calculating the average."""""


class average:

    def __init__(self, length, sum):
        self.length = length
        self.sum = sum
        self.mean = 0

    def calAverage(self):
        self.mean = self.sum / self.length
        return self.mean
