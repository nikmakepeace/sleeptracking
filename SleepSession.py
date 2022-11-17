

class SessionSummary:
    """Represents the summary of a sleep session. Created from SleepSession data and stored"""
    pass

class SummaryStorer:
    """Uses the engine passed in to save a SessionSummary"""

    def __init__(self, engine):
        self.engine = engine

    def persistSummary(self, summary: SessionSummary):
        # construct the SQL to save the instance data in SessionSummary and use self.engine to save it
        pass

class SleepSession:
    """Represents a single session of sleep. Contains all the SleepRecords for that session"""
    pass


class SessionSummaryFactory:
    def createSessionSummary(session: SleepSession) -> SessionSummary:
        pass
