from sqlalchemy import text


class NightRetriever:
    """Uses the connection passed in to retrieve a whole Night of SleepRecords"""
    def __init__(self, conn, night_of):
        self.conn = conn
        self.night_of = night_of

    def fetch_sleep_records(self):
        sleep_record_rows = []
        sql = text('SELECT * from sleep_data where Night_Of = :night_of ORDER BY dt ASC')
        result = self.conn.execute(sql, [{'night_of': self.night_of}])
        for row in result:
            sleep_record_rows.append(row)

        return sleep_record_rows
