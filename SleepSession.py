class SleepSession:
    """Represents a single session of sleep. Contains all the SleepRecords for that session"""
    def __init__(self, night):
        self.night = night

    def add_record(self):
        pass


class SessionSummary:
    """Represents the summary of a sleep session. Created from SleepSession data and stored"""
    def __init__(self, session: SleepSession):
        self.session = session
        pass


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
