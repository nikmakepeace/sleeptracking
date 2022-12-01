from sqlalchemy.future import Engine

import prod_db
import orm_setup
import sleep_record
import sleep_session

engine: Engine = prod_db.get_engine()
orm_setup.Base.metadata.drop_all(engine)
orm_setup.Base.metadata.create_all(engine)
