"""Totally fake stub for a real database. Obviously nonsense"""
def create_engine(dsn):
    engine = ""
    return engine


def run_sql(sql, engine):
    rows = [
        [12345, 'rando', 1, True, 3, False],
        [12346, 'rando', 5, False, 7, True],
        [12347, 'rando', 9, True, 11, True],
        [12348, 'rando', 13, False, 15, False]
    ]
    return rows