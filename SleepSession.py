import SleepMaths
import SleepRecord


class SleepSession:
    """Represents a single session of sleep. Contains all the SleepRecords for that session"""
    def __init__(self, night):
        self.night = night

    def add_record(self, record: SleepRecord):
        pass


class SessionSummary:
    """Represents the summary of a sleep session. Created from SleepSession data and stored"""
    def __init__(self, session: SleepSession):
        self.session = session
        self.summary_params = ['mean_spo2', 'mean_pr', 'has_spo2_warning', 'has_pr_warning', 'has_4pc_sp02_drop', 'has_10bpm_pr_drop']

    def calculate_average(self, param, aggregator: SleepMaths.Aggregator):
        pass

    def calculate_averages(self, aggregator: SleepMaths.Aggregator):
        for param in ['spo2', 'pr']
            self.calculate_average(param, aggregator)

class SessionSummaryFactory:
    def create_session_summary(self, session: SleepSession) -> SessionSummary:
        return SessionSummary(session)


class SummaryStorer:
    """Uses the engine passed in to save a SessionSummary"""

    def __init__(self, engine):
        self.engine = engine

    def persist_summary(self, summary: SessionSummary):
        # construct the SQL to save the instance data in SessionSummary and use self.engine to save it
        pass
