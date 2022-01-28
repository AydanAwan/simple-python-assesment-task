"""an interface that gets the user input then interacts with the database and methods to display results."""


from methods.average import average
from methods.count import count
from methods.length import length
from methods.maxMinValue import maxMinValue
from methods.meanDeviation import meanDeviation
from methods.median import median
from methods.range import range
from methods.sort import sort
from methods.standardDeviation import standardDeviation
from methods.sum import sum
from methods.sumOfSquares import sumOfSquares
from methods.variance import variance
from database import database


class interface:

    def __init__(self, dataset):
        if dataset == "default":
            self.database = database("default")
            print(self.database.get_dataSet())
        elif not isinstance(dataset, list):
            raise TypeError("input must be either a list of numbers or \" default \"")
        elif not dataset:
            raise IndexError("there are no values in your data list")
        elif all(isinstance(element, (int, float)) for element in dataset):
            self.database = database(dataset)
            print(self.database.get_dataSet())
        else:
            raise ValueError('all elements inside your list are not integers')

    def find_length(self):
        if self.database.get_length():
            return(self.database.get_length())
        else:
            x = length(self.database.get_dataSet()).calLength()
            self.database.set_length(x)
            return(self.database.get_length())

    def find_sort(self):
        if self.database.get_sort():
            return(self.database.get_sort())
        else:
            x = sort(self.database.get_dataSet()).sortData()
            self.database.set_sort(x)
            return(self.database.get_sort())

    def find_sum(self):
        if self.database.get_sum():
            return(self.database.get_sum())
        else:
            x = sum(self.database.get_dataSet()).calSum()
            self.database.set_sum(x)
            return(self.database.get_sum())

    def find_count(self, countvariable):
        x = count(self.database.get_dataSet(), countvariable).calCount()
        return(x)

    def find_average(self):
        if self.database.get_average():
            return(self.database.get_average())
        else:
            if self.database.get_sum() is False:
                self.find_sum()
            if self.database.get_length() is False:
                self.find_length()
            x = average(self.database.get_length(), self.database.get_sum()).calAverage()
            self.database.set_average(x)
            return(self.database.get_average())

    def find_median(self):
        if self.database.get_median():
            return(self.database.get_median())
        else:
            if self.database.get_sort() is False:
                self.find_sort()
            if self.database.get_length() is False:
                self.find_length()
            x = median(self.database.get_sort(), self.database.get_length()).calMedian()
            self.database.set_median(x)
            return(self.database.get_median())

    def find_max(self):
        if self.database.get_max():
            return(self.database.get_max())
        else:
            if self.database.get_sort() is False:
                self.find_sort()
            if self.database.get_length() is False:
                self.find_length()
            x = maxMinValue(self.database.get_sort()).getMax(self.database.get_length())
            self.database.set_max(x)
            return(self.database.get_max())

    def find_min(self):
        if self.database.get_min():
            return(self.database.get_min())
        else:
            if self.database.get_sort() is False:
                self.find_sort()
            x = maxMinValue(self.database.get_sort()).getMin()
            self.database.set_min(x)
            return(self.database.get_min())

    def find_range(self):
        if self.database.get_range():
            return(self.database.get_range())
        else:
            if self.database.get_sort() is False:
                self.find_sort()
            if self.database.get_length() is False:
                self.find_length()
            x = range(self.database.get_sort(), self.database.get_length()).calRange()
            self.database.set_range(x)
            return(self.database.get_range())

    def find_sos(self):
        if self.database.get_sos():
            return(self.database.get_sos())
        else:
            if self.database.get_average() is False:
                self.find_average()
            if self.database.get_length() is False:
                self.find_length()
            x = sumOfSquares(self.database.get_average(), self.database.get_dataSet()).calSumOfSquares()
            self.database.set_sos(x)
            return(self.database.get_sos())

    def find_variance(self):
        if self.database.get_variance():
            return(self.database.get_variance())
        else:
            if self.database.get_sos() is False:
                self.find_sos()
            if self.database.get_length() is False:
                self.find_length()
            x = variance(self.database.get_sos(), self.database.get_length()).calVariance()
            self.database.set_variance(x)
            return(self.database.get_variance())

    def find_meanDeviation(self):
        if self.database.get_meanDeviation():
            return(self.database.get_meanDeviation())
        else:
            if self.database.get_average() is False:
                self.find_average()
            if self.database.get_length() is False:
                self.find_length()
            x = meanDeviation(self.database.get_average(), self.database.get_length(), self.database.get_dataSet()).calMeanDev()
            self.database.set_meanDeviation(x)
            return(self.database.get_meanDeviation())

    def find_standardDeviation(self):
        if self.database.get_standardDeviation():
            return(self.database.get_standardDeviation())
        else:
            if self.database.get_sos() is False:
                self.find_sos()
            if self.database.get_length() is False:
                self.find_length()
            x = standardDeviation(self.database.get_sos(), self.database.get_length()).calStaDev()
            self.database.set_standardDeviation(x)
            return(self.database.get_standardDeviation())

    """except count, the methods in this are set up so that if you try and find a calculation that has already been done it will display that calculation that has been saved in the database if they havent been done then they will look to see if the prerequisit calculations had been done and if they havent done them then calculate their find and save the value to teh database, thsi is so no calculation has to be done twice and saves costs at run time."""
