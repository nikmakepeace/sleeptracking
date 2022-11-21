
class Aggregator:
    """Class to contain functions that operate on column data and reduce to a single value"""

    def mean(self, values: list) -> float:
        return sum(values) / len(values)

    def min(self, values: list) -> int:
        return min(values)

    def max(self, values: list) -> int:
        return max(values)

    def count(self, values: list) -> int:
        return len(values)

