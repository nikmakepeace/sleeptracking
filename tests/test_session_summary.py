import unittest
import random
from datetime import datetime
from time import time

from sleep_session import SleepSession
from sleep_record import SleepRecord
from session_summary import SessionSummary, SessionSummaryFactory, SummaryRepository
from sleep_maths import Aggregator
from stub_sqlalchemy import create_engine


class TestSessionSummary(unittest.TestCase):
    def test_constructor(self):
        session = SleepSession('rando')
        summary = SessionSummary(session)
        self.assertIsInstance(summary._session, SleepSession)
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


class TestSummaryRepository(unittest.TestCase):
    """Of very dubious value - doesn't actually test the persistence at all, just the calling of the factory methods"""
    def test_persistence(self):
        # create a session summary, populate the fields, persist it, and then read it back and compare
        now = datetime.now()
        session = SleepSession(now)
        expected_summary = SessionSummaryFactory.create_session_summary(session)

        random.seed(time() * 131072)
        expected_summary.mean_pr = random.uniform(45.0, 75.0)
        expected_summary.mean_spo2 = random.uniform(95.0, 100.0)

        engine = create_engine('ignored')
        conn = engine.connect()
        conn.set_result([{'name': now, 'mean_pr': expected_summary.mean_pr, 'mean_spo2': expected_summary.mean_spo2}])
        summary_repo = SummaryRepository(conn)
        summary_repo.persist_summary(expected_summary)

        # now read it back and compare (assumes session.night is unique in the DB)
        actual_summary = summary_repo.retrieve_summary(expected_summary.name)
        self.assertEqual(expected_summary.name, actual_summary.name)
        self.assertEqual(expected_summary.mean_pr, actual_summary.mean_pr)
        self.assertEqual(expected_summary.mean_spo2, actual_summary.mean_spo2)
