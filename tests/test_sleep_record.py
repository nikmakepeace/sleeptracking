import unittest
from types import SimpleNamespace

from sleep_record import SleepRecord, SleepRecordFactory


class TestSleepRecord(unittest.TestCase):
    def test_constructor(self):
        # test that the values are being stored
        record = SleepRecord(123, '11/07/2022', 345, True, 456, False)
        self.assertEqual(123, record.time)
        self.assertEqual('11/07/2022', record.night_of)
        self.assertEqual(345, record.spo2)
        self.assertEqual(True, record.spo2_reminder)
        self.assertEqual(456, record.pulse_rate)
        self.assertEqual(False, record.pulse_rate_reminder)


class TestSleepRecordFactory(unittest.TestCase):
    def test_factory_method_returns_sleep_record(self):
        row = {'dt': 0, 'night_of': 'rando', 'spo2': 1, 'spo2_reminder': False, 'pulse_rate': 2, 'pr_reminder': True}
        # use SimpleNamespace to convert the dict into a dot-accessible object for the SleepRecord constructor
        result = SleepRecordFactory.create_sleep_record(SimpleNamespace(**row))
        self.assertIsInstance(result, SleepRecord)
        self.assertEqual(0, result.time)
        self.assertEqual('rando', result.night_of)
        self.assertEqual(1, result.spo2)
        self.assertEqual(False, result.spo2_reminder)
        self.assertEqual(2, result.pulse_rate)
        self.assertEqual(True, result.pulse_rate_reminder)

