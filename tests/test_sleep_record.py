import unittest

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
        row = [0, 'rando', 1, False, 2, True]
        result = SleepRecordFactory.create_sleep_record(row)
        self.assertIsInstance(result, SleepRecord)
        self.assertEqual('rando', result.night_of)
