"""classs and method for calculating the median."""""


class median:

    def __init__(self, sorteddataset, length):
        self.sorteddata = sorteddataset
        self.length = length

    def calMedian(self):
        if self.length % 2 == 1:
            return self.sorteddata[int((self.length - 1) / 2)]
        else:
            lower = self.sorteddata[int(self.length / 2 - 1)]
            upper = self.sorteddata[int(self.length / 2)]
            return (lower + upper) / 2
