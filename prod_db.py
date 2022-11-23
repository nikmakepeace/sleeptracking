import sqlalchemy
from sqlalchemy.future import Engine

import env_vars

if 'engine' not in locals():
    engine: Engine = sqlalchemy.create_engine(env_vars.dsn, echo=True, future=True)


def get_engine():
    return engine
