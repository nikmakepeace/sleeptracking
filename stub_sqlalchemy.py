"""Totally fake stub for a real database. Obviously nonsense"""
from types import SimpleNamespace


def create_engine(dsn):
    return Engine(dsn)


class Engine:
    def __init__(self, dsn):
        self.dsn = dsn
        pass

    def connect(self):
        return Connection(self)


class Connection:
    def __init__(self, engine):
        self.engine = engine
        self.result = []
        self.last_issued_sql = ''

    def execute(self, sql, result=None):
        self.last_issued_sql = sql
        if result is None:
            result = self.result
        return result

    def set_result(self, result_rows: dict):
        # convert it into a dot-addressable object as though it were coming from a database
        for row in result_rows:
            self.result.append(SimpleNamespace(**row))

    def clear_result(self):
        self.result = []


def sample_result():
    return [12345, 'rando', 1, True, 3, False], \
        [12346, 'rando', 5, False, 7, True],    \
        [12347, 'rando', 9, True, 11, True],    \
        [12348, 'rando', 13, False, 15, False]
