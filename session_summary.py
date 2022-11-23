import sleep_maths
from sleep_session import SleepSession
from sleep_maths import Aggregator


class SessionSummary:
    """Represents the summary of a sleep session. Created from SleepSession data and stored"""
    def __init__(self, session: SleepSession):
        self.name = session.night
        self._session = session
        self.mean_spo2 = None
        self.mean_pr = None


    def calculate_averages(self, aggregator: Aggregator):
        self._calculate_mean_spo2(aggregator)
        self._calculate_mean_pr(aggregator)

    def _calculate_mean_spo2(self, aggregator: Aggregator):
        spo2_records = []
        for record in self._session.records:
            spo2_records.append(record.spo2)
        self.mean_spo2 = aggregator.mean(spo2_records)

    def _calculate_mean_pr(self, aggregator: Aggregator):
        pr_records = []
        for record in self._session.records:
            pr_records.append(record.pulse_rate)
        self.mean_pr = aggregator.mean(pr_records)
class SessionSummaryFactory:
    @staticmethod
    def create_session_summary(session: SleepSession) -> SessionSummary:
        return SessionSummary(session)


class SummaryRepository:
    """Uses the engine passed in to save a SessionSummary"""
    def __init__(self, conn):
        self.conn = conn

    def persist_summary(self, summary: SessionSummary):
        # construct the SQL to save the instance data in SessionSummary and use self.engine to save it
        pass

    def retrieve_summary(self, session_night) -> SessionSummary:
        # construct the SQL to fetch the session data using self.engine, and populate SessionSummary and return
        return SessionSummary(SleepSession('fakedata'))
