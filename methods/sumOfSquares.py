"""class and metheod for calculating the sum of squares used in the variance and standard deviation calcualtions."""


class sumOfSquares:

    def __init__(self, mean, dataset):
        self.mean = mean
        self.data = dataset

    def calSumOfSquares(self):
        y = 0
        for x in self.data:
            y += (x - self.mean)**2
        return y
