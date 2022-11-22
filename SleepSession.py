import SleepRecord


class SleepSession:
    """Represents a single session of sleep. Contains all the SleepRecords for that session"""
    def __init__(self, night):
        self.night = night
        self.records = []

    def add_record(self, record: SleepRecord):
        self.records.append(record)
