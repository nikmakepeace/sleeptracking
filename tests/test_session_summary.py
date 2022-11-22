import unittest
import random
import time

from sleep_session import SleepSession
from sleep_record import SleepRecord
from session_summary import SessionSummary, SessionSummaryFactory, SummaryRepository
from sleep_maths import Aggregator
from sqlalchemy import create_engine, run_sql


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


class TestSummaryStorer(unittest.TestCase):
    def test_persistence(self):
        # create a session summary, populate the fields, persist it, and then read it back and compare
        engine = create_engine('blah di blah')
        session = SleepSession((time.time()*33554432 % 1048575))
        expected_summary = SessionSummaryFactory.create_session_summary(session)
        random.seed(time.time() * 131072)
        expected_summary.mean_pr = random.uniform(45.0, 75.0)
        expected_summary.mean_spo2 = random.uniform(95.0, 100.0)
        summary_repo = SummaryRepository(engine)
        summary_repo.persist_summary(expected_summary)

        # now read it back and compare (assumes session.night is unique in the DB)
        actual_summary = summary_repo.retrieve_summary(expected_summary.name)
        self.assertEqual(expected_summary.name, actual_summary.name)
        self.assertEqual(expected_summary.mean_pr, actual_summary.mean_pr)
        self.assertEqual(expected_summary.mean_spo2, actual_summary.mean_spo2)


