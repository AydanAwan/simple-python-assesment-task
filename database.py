"""class and methods for storing data values and completed calculations."""


class database:

    def __init__(self, customData):
        if customData == "default":
            self.dataSet = list(range(1, 51))
        else:
            self.dataSet = customData
        self.average = False
        self.count = False
        self.length = False
        self.min = False
        self.max = False
        self.meanDeviation = False
        self.median = False
        self.range = False
        self.sort = False
        self.standardDeviation = False
        self.sum = False
        self.variance = False
        self.sos = False

    def get_dataSet(self):
        return self.dataSet

    def get_average(self):
        return self.average

    def get_length(self):
        return self.length

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_meanDeviation(self):
        return self.meanDeviation

    def get_median(self):
        return self.median

    def get_range(self):
        return self.range

    def get_sort(self):
        return self.sort

    def get_standardDeviation(self):
        return self.standardDeviation

    def get_sum(self):
        return self.sum

    def get_sos(self):
        return self.sos

    def get_variance(self):
        return self.variance

    def set_average(self, newVal):
        self.average = newVal

    def set_length(self, newVal):
        self.length = newVal

    def set_min(self, newVal):
        self.min = newVal

    def set_max(self, newVal):
        self.max = newVal

    def set_meanDeviation(self, newVal):
        self.meanDeviation = newVal

    def set_median(self, newVal):
        self.median = newVal

    def set_range(self, newVal):
        self.range = newVal

    def set_sort(self, newVal):
        self.sort = newVal

    def set_standardDeviation(self, newVal):
        self.standardDeviation = newVal

    def set_sum(self, newVal):
        self.sum = newVal

    def set_sos(self, newVal):
        self.sos = newVal

    def set_variance(self, newVal):
        self.variance = newVal

    """all the methods for setting and getting all the data that comes from this programme, note that count is missing that is because we dont want to set the count as the count will change everytime you look for a differrent variable."""
