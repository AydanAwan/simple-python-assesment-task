"""classs and method for calculating the range."""""


class range:

    def __init__(self, sortedDatalist, length):
        self.sortedData = sortedDatalist
        self.length = length

    def calRange(self):
        return self.sortedData[self.length - 1] - self.sortedData[0]
