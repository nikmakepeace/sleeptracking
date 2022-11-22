import unittest

from SleepSession import SleepSession, SessionSummary, SessionSummaryFactory
from SleepRecord import SleepRecord
from SleepMaths import Aggregator


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


class TestSessionSummary(unittest.TestCase):
    def test_constructor(self):
        session = SleepSession('rando')
        summary = SessionSummary(session)
        self.assertIsInstance(summary.session, SleepSession)
        self.assertIsNone(summary.mean_pr)
        self.assertIsNone(summary.mean_spo2)

    def test_calculate_averages(self):
        session = SleepSession('rando')
        record = SleepRecord(0, '', 10, False, 0, True)
        session.add_record(record)
        record = SleepRecord(0, '', 17, False, 13, True)
        session.add_record(record)
        record = SleepRecord(0, '', 93, False, 5, True)
        session.add_record(record)
        summary = SessionSummary(session)
        aggregator = Aggregator()
        summary.calculate_averages(aggregator)
        self.assertEqual(40, summary.mean_spo2)
        self.assertEqual(6, summary.mean_pr)

class TestSessionSummaryFactory(unittest.TestCase):
    def test_factory_method(self):
        session = SleepSession('rando')
        summary = SessionSummaryFactory.create_session_summary(session)
        self.assertIsInstance(summary, SessionSummary)
