if __name__ == '__main__':
    # create a DB engine
    # select all the values of the nights from the store using SQL like SELECT DISTINCT Night_Of ...
    # iterate over those values:
    #   grab one night at a time like so:
    #       instantiate NightRetriever
    #       instantiate SleepSession
    #       get the rows from the DB for the night
    #       iterate over the rows
    #           Use SleepRecordFactory to create a SleepRecord for each row
    #           add each SleepRecord to the SleepSession
    #       now you have a SleepSession with all the SleepRecords for the night
    #       Use SessionSummaryFactory to create a SessionSummary instance
    #       Pass in Aggregator and do the aggregation that you want, adding to instance variables in SessionSummary
    #       Save the summary by creating a SummaryStorer and passing in the engine and the SessionSummary
    pass

class SleepRecord:
    """A single record from a sleep monitor"""

    def __init__(self, time: int, night_of: str, spo2: int, spo2_reminder: bool, pulse_rate: int, pulse_rate_reminder: bool):
        self.time = time
        self.spo2 = spo2
        self.night_of = night_of
        self.spo2_reminder = spo2_reminder
        self.pulse_rate = pulse_rate
        self: pulse_rate_reminder = pulse_rate_reminder


class NightRetriever:
    """Uses the engine passed in to retrieve a whole Night of SleepRecords"""

    def __init__(self, engine, night_of):
        self.engine = engine
        self.night_of = night_of
        pass


class SessionSummary:
    """Represents the summary of a sleep session. Created from SleepSession data and stored"""
    pass


class SummaryStorer:
    """Uses the engine passed in to save a SessionSummary"""

    def __init__(self, engine, summary: SessionSummary):
        pass


class SleepSession:
    """Represents a single session of sleep. Contains all the SleepRecords for that session"""
    pass


class Aggregator:
    """Class to contain functions that operate on column data and reduce to a single value"""

    def mean(values: list) -> float:
        return sum(values) / len(values)

    def min(values: list) -> int:
        return min(values)

    def max(values: list) -> int:
        return max(values)

    def count(values: list) -> int:
        return len(values)


class SleepRecordFactory:
    def createSleepRecord(row) -> SleepRecord:
        pass
