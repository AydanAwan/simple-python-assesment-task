"""classs and method for calculating the sum of a given dataset."""""


class sum:

    def __init__(self, dataset):
        self.data = dataset

    def calSum(self):
        sum = 0
        for x in self.data:
            sum += x
        return sum
