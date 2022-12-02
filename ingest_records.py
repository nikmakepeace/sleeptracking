"""Ingests the raw sleep records and creates empty sessions"""
import prod_db
from sleep_record import SleepRecord
from sleep_session import SleepSession
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.future import Engine
from datetime import datetime

import csv

engine: Engine = prod_db.get_engine()


if '__main__' == __name__:

    with Session(engine) as session:
        # grab each line of CSV and make a SleepRecord
        with open('sleep_data.csv', newline='', encoding='utf-8-sig') as csvfile:
            sleep_data_reader = csv.DictReader(csvfile, dialect='excel')
            for row in sleep_data_reader:

                sleep_record = SleepRecord(dt=datetime.strptime(row['dt'], '%d/%m/%Y %H:%M'), spo2=int(row['SpO2']),
                                           pulse_rate=int(row['Pulse_Rate']), motion=int(row['Motion']),
                                           spo2_reminder=bool(row['SPO2_Reminder']),
                                           pr_reminder=bool(row['PR_Reminder']))
                session.add(sleep_record)

                night_of = sleep_record.calculate_night_of()
                # if there isn't a SleepSession for the night yet, make one

                stmt = select(SleepSession).where(SleepSession.night_of == night_of)
                try:
                    sleep_session = session.scalars(stmt).one()
                except NoResultFound:
                    sleep_session = SleepSession(night_of=night_of)
                    session.add(sleep_session)

                sleep_record.sleep_session = sleep_session

        session.commit()
