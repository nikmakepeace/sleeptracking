import unittest

from sleep_session import SleepSession
from sleep_record import SleepRecord


class TestSleepSession(unittest.TestCase):
    def test_constructor(self):
        session = SleepSession('rando')
        self.assertEqual('rando', session.night)

    def test_add_record(self):
        record = SleepRecord(0, 'ridonkulous', 12, False, 13, True)
        session = SleepSession('rando')
        session.add_record(record)
        self.assertIsInstance(session.records[0], SleepRecord)
        self.assertEqual(1, len(session.records))
