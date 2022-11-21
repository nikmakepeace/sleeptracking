class SleepRecord:
    """A single record from a sleep monitor"""
    def __init__(self, time: int, night_of: str, spo2: int, spo2_reminder: bool, pulse_rate: int,
                 pulse_rate_reminder: bool):
        self.time = time
        self.spo2 = spo2
        self.night_of = night_of
        self.spo2_reminder = spo2_reminder
        self.pulse_rate = pulse_rate
        self.pulse_rate_reminder = pulse_rate_reminder


class SleepRecordFactory:
    def create_sleep_record(self, row) -> SleepRecord:
        return SleepRecord(row[0], row[1], row[2], row[3], row[4], row[5])
