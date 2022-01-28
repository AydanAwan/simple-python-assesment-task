"""class and metheod for calculating the vaiance."""


class variance:

    def __init__(self, sumofsquares, length):
        self.length = length
        self.sos = sumofsquares

    def calVariance(self):
        return self.sos / (self.length - 1)
