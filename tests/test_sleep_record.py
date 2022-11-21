import unittest

from SleepRecord import SleepRecord, SleepRecordFactory


class TestSleepRecord(unittest.TestCase):
    def test_constructor(self):
        # test that the values are being stored
        record = SleepRecord(123, '11/07/2022', 345, True, 456, False)
        self.assertEqual(record.time, 123)
        self.assertEqual(record.night_of, '11/07/2022')
        self.assertEqual(record.spo2, 345)
        self.assertEqual(record.spo2_reminder, True)
        self.assertEqual(record.pulse_rate, 456)
        self.assertEqual(record.pulse_rate_reminder, False)


class TestSleepRecordFactory(unittest.TestCase):
    def test_factory_method(self):
        factory = SleepRecordFactory()
        row = []
        result = factory.create_sleep_record(row)
        self.assertTrue(isinstance(result, SleepRecord))
