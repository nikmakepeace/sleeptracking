import unittest

from sleep_maths import Aggregator


class TestAggregator(unittest.TestCase):
    def setUp(self):
        self.set_1 = {
            'values': [1, 1, 2, 2, 9, 21],
            'mean': 6.0,
            'count': 6,
            'min': 1,
            'max': 21
        }
        self.set_2 = {
            'values': [100, 30, 5, 0],
            'mean': 33.75,
            'count': 4,
            'min': 0,
            'max': 100
        }
        self.aggregator = Aggregator()

    def test_mean(self):
        self.assertEqual(self.set_1['mean'], self.aggregator.mean(self.set_1['values']))
        self.assertEqual(self.set_2['mean'], self.aggregator.mean(self.set_2['values']))

    def test_count(self):
        self.assertEqual(self.set_1['count'], self.aggregator.count(self.set_1['values']))
        self.assertEqual(self.set_2['count'], self.aggregator.count(self.set_2['values']))

    def test_min(self):
        self.assertEqual(self.set_1['min'], self.aggregator.min(self.set_1['values']))
        self.assertEqual(self.set_2['min'], self.aggregator.min(self.set_2['values']))

    def test_max(self):
        self.assertEqual(self.set_1['max'], self.aggregator.max(self.set_1['values']))
        self.assertEqual(self.set_2['max'], self.aggregator.max(self.set_2['values']))

    # TODO test handling lists with non-numeric items
