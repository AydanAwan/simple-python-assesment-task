"""class and metheod for calculating the standard devieation."""
import math


class standardDeviation:

    def __init__(self, sumofsquares, length):
        self.length = length
        self.sos = sumofsquares

    def calStaDev(self):
        return math.sqrt(self.sos / self.length)
