import sqlalchemy
import env_vars

if 'engine' not in locals():
    engine = sqlalchemy.create_engine(env_vars.dsn, echo=True, future=True)


def get_connection():
    return engine.connect()
