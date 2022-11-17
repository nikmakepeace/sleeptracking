
class Aggregator:
    """Class to contain functions that operate on column data and reduce to a single value"""

    def mean(values: list) -> float:
        return sum(values) / len(values)

    def min(values: list) -> int:
        return min(values)

    def max(values: list) -> int:
        return max(values)

    def count(values: list) -> int:
        return len(values)

