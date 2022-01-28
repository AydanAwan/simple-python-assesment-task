"""testing for all the statistical methods."""


import unittest
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


class TestMethods(unittest.TestCase):

    def test_length(self):
        result = length([1, 2, 3, 4, 5, 6]).calLength()
        self.assertEquals(result, 6)

    def test_sort(self):
        result = sort([4, 2, 3, 1, 5, 6]).sortData()
        self.assertEquals(result, [1, 2, 3, 4, 5, 6])

    def test_sum(self):
        result = sum([1, 2, 3, 4, 5, 6]).calSum()
        self.assertEquals(result, 21)

    def test_average(self):
        result = average(7, 21).calAverage()
        self.assertEquals(result, 3)

    def test_min(self):
        result = maxMinValue([1, 2, 3, 4, 5, 6]).getMin()
        self.assertEquals(result, 1)

    def test_max(self):
        result = maxMinValue([1, 2, 3, 4, 5, 6]).getMax(6)
        self.assertEquals(result, 6)

    def test_median_odd(self):
        result = median([1, 2, 3, 4, 5, 6, 7], 7).calMedian()
        self.assertEquals(result, 4)

    def test_median_even(self):
        result = median([1, 2, 3, 4, 5, 6], 6).calMedian()
        self.assertEquals(result, 3.5)

    def test_range(self):
        result = range([1, 2, 3, 4, 5, 6], 6).calRange()
        self.assertEquals(result, 5)

    def test_count(self):
        result = count([1, 4, 2, -4, 4, 2, 3, 4, 5, 6], 4).calCount()
        self.assertEquals(result, 3)

    def test_sumOfSquares(self):
        result = sumOfSquares(3, [1, 2, 3, 4, 5]).calSumOfSquares()
        self.assertEquals(result, 10)

    def test_variation(self):
        result = variance(10, 5).calVariance()
        self.assertEquals(result, 2.5)

    def test_meanDeviation(self):
        result = meanDeviation(3, 5, [1, 2, 3, 4, 5]).calMeanDev()
        self.assertEquals(result, 1.2)

    def test_standardDeviation(self):
        result = standardDeviation(20, 5).calStaDev()
        self.assertEquals(result, 2)


if __name__ == '__main__':
    unittest.main()
