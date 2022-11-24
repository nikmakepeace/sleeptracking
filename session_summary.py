from sqlalchemy import text, engine
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

    @staticmethod
    def create_session_summary_from_computed_data(data) -> SessionSummary:
        summary = SessionSummary(SleepSession(data.name))
        summary.mean_spo2 = data.mean_spo2
        summary.mean_pr = data.mean_pr
        return summary


class SummaryRepository:
    """Uses the engine passed in to save a SessionSummary"""
    def __init__(self, conn: engine.Connection):
        self.conn = conn

    def persist_summary(self, summary: SessionSummary):
        # construct the SQL to save the instance data in SessionSummary and use self.engine to save it
        param_sql = 'INSERT into sleep_state (name, mean_pr, mean_spo2) ' \
                    'VALUES (:name, :mean_pr, :mean_spo2) ' \
                    'ON CONFLICT (name) DO ' \
                    'UPDATE SET mean_pr = EXCLUDED.mean_pr, mean_spo2 = EXCLUDED.mean_spo2 '

        params = [{'name': summary.name, 'mean_pr': summary.mean_pr, 'mean_spo2': summary.mean_spo2}]
        sql = text(param_sql)
        self.conn.execute(sql, params)

    def retrieve_summary(self, session_night) -> SessionSummary:
        # construct the SQL to fetch the session data using self.conn, and populate SessionSummary and return
        sql = text('SELECT id, name, mean_pr, mean_spo2 FROM summary WHERE name = :night', {'night': session_night})
        result = self.conn.execute(sql)
        return SessionSummaryFactory.create_session_summary_from_computed_data(result[0])
