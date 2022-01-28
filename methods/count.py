"""classs and method for calculating the count of any given variable."""""


class count:

    def __init__(self, dataset, countvariable):
        self.data = dataset
        self.countvariable = countvariable

    def calCount(self):
        counter = 0
        for x in self.data:
            if x == self.countvariable:
                counter += 1
        return counter
