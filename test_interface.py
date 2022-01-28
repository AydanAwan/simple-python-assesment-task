"""testing for all the find methods in the interface."""


import unittest
from interface import interface


class TestInterface(unittest.TestCase):

    def test_findlength(self):
        result = interface([1, 2, 3, 4, 5, 6]).find_length()
        self.assertEquals(result, 6)

    def test_findsort(self):
        result = interface([4, 2, 3, 1, 5, 6]).find_sort()
        self.assertEquals(result, [1, 2, 3, 4, 5, 6])

    def test_findsum(self):
        result = interface([1, 2, 3, 4, 5, 6]).find_sum()
        self.assertEquals(result, 21)

    def test_findaverage(self):
        result = interface([1, 2, 1, 2, 4, 5, 6]).find_average()
        self.assertEquals(result, 3)

    def test_findmin(self):
        result = interface([1, 2, 3, 4, 5, 6]).find_min()
        self.assertEquals(result, 1)

    def test_findmax(self):
        result = interface([1, 2, 3, 4, 5, 6]).find_max()
        self.assertEquals(result, 6)

    def test_findmedian_odd(self):
        result = interface([1, 2, 3, 4, 5, 6, 7]).find_median()
        self.assertEquals(result, 4)

    def test_findmedian_even(self):
        result = interface([1, 2, 3, 4, 5, 6]).find_median()
        self.assertEquals(result, 3.5)

    def test_findrange(self):
        result = interface([1, 2, 3, 4, 5, 6]).find_range()
        self.assertEquals(result, 5)

    def test_findcount(self):
        result = interface([1, 4, 2, -4, 4, 2, 3, 4, 5, 6]).find_count(4)
        self.assertEquals(result, 3)

    def test_findsumOfSquares(self):
        result = interface([1, 2, 3, 4, 5]).find_sos()
        self.assertEquals(result, 10)

    def test_findvariation(self):
        result = interface([1, 2, 3, 4, 5]).find_variance()
        self.assertEquals(result, 2.5)

    def test_findmeanDeviation(self):
        result = interface([1, 2, 3, 4, 5]).find_meanDeviation()
        self.assertEquals(result, 1.2)

    def test_findstandardDeviation(self):
        result = interface([1, 2, 3, 4, 5, 6, 7]).find_standardDeviation()
        self.assertEquals(result, 2)

# testing all the functions work given no predone calculations

    def test_already_calculated(self):
        testinter = interface([1, 2, 3, 4, 5, 6, 7])
        testinter.database.set_standardDeviation(3)
        result = testinter.find_standardDeviation()
        self.assertEquals(result, 3)

# testing that the functions given that their culculations had been done before would not rerun them

    def test_already_set_variables(self):
        testinter = interface([1, 2, 3, 4, 5, 6, 7])
        testinter.database.set_sos(18)
        testinter.database.set_length(2)
        result = testinter.find_standardDeviation()
        self.assertEquals(result, 3)

# testing that given the required variables for a function were already acalculated it would work using them and not drecalculating them
# im only testing these last two on one of the equations to save time but if this code was going to be deployed id do it for all of them

    def test_default_dataset(self):
        testinter = interface("default")
        result = testinter.database.get_dataSet()
        self.assertEquals(result, list(range(1, 51)))

    def test_dataset_contains_nonnumber(self):
        self.failUnlessRaises(ValueError, interface, [1, 3, 5, 34, "hello", 0, 34, 64, 3, 6, 456, -9, 47.34])

    def test_input_emptylist(self):
        self.failUnlessRaises(TypeError, interface, 34)

    def test_inpu_nonlist(self):
        self.failUnlessRaises(IndexError, interface, [])

# testing that if the input dataset is not applicable then we get errors as to why and testing that you can call the default dataset


if __name__ == '__main__':
    unittest.main()
