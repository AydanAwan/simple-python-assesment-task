"""classs and method for calculating the max and min values."""""


class maxMinValue:

    def __init__(self, sortedDatalist):
        self.sortedData = sortedDatalist

    def getMax(self, length):
        return self.sortedData[length - 1]

    def getMin(self):
        return self.sortedData[0]
