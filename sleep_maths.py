
class Aggregator:
    """Class to contain functions that operate on column data and reduce to a single value"""

    def mean(self, values: list) -> float:
        """Produces the mean of all the numbers in a list"""
        return sum(values) / len(values)

    def min(self, values: list) -> int:
        """Produces the smallest number of all the numbers in a list"""
        return min(values)

    def max(self, values: list) -> int:
        """Produces the largest number of all the numbers in a list"""
        return max(values)

    def count(self, values: list) -> int:
        """Produces the number of numbers in the list"""
        return len(values)
