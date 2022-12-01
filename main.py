"""Go through sleep records and fill out session aggregates"""
import prod_db
import sleep_maths
from sleep_session import SleepSession
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.future import Engine

engine: Engine = prod_db.get_engine()


if __name__ == '__main__':
    # get all the distinct values of night_of from SleepRecord
    # for each night_of:
    #   select all the sleep records
    #       add each SleepRecord to the SleepSession
    #   now you have a SleepSession with all the SleepRecords for the night
    #   fetch a SessionSummary instance for night_of or create a new one and add it to the store
    #   pass in Aggregator and do the aggregation that you want, adding the results to SessionSummary
    #   save the SessionSummary

    with Session(engine) as session:
        aggregator = sleep_maths.Aggregator()

        for sleep_session in session.scalars(select(SleepSession)):
            sleep_session.calculate_averages(aggregator)

        session.commit()
