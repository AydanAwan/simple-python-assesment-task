"""classs and method for calculating the length of the dataset."""""


class length:

    def __init__(self, datalist):
        self.data = datalist

    def calLength(self):
        return len(self.data)
