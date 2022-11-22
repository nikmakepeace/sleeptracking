from stub_sqlalchemy import run_sql


class NightRetriever:
    """Uses the engine passed in to retrieve a whole Night of SleepRecords"""
    def __init__(self, engine, night_of):
        self.engine = engine
        self.night_of = night_of

    def fetch_sleep_records(self):
        sql = 'SELECT * from sleep_data where Night_Of = {self.night_of} ORDER BY dt ASC'
        sleep_record_rows = run_sql(sql, self.engine)
        return sleep_record_rows
