from sqlalchemy import text

import prod_db
import sleep_session
import session_summary
import sleep_maths
import night_retriever
import sleep_record

if __name__ == '__main__':
    # create a DB engine
    # select all the values of the nights from the store using SQL like SELECT DISTINCT Night_Of ...
    # iterate over those values:
    #   grab one night at a time like so:
    #       instantiate NightRetriever
    #       instantiate SleepSession
    #       get the rows from the DB for the night
    #       iterate over the rows
    #           Use SleepRecordFactory to create a SleepRecord for each row
    #           add each SleepRecord to the SleepSession
    #       now you have a SleepSession with all the SleepRecords for the night
    #       Use SessionSummaryFactory to create a SessionSummary instance
    #       Pass in Aggregator and do the aggregation that you want, adding to instance variables in SessionSummary
    #       Save the summary by creating a SummaryStorer and passing in the engine and the SessionSummary

    engine = prod_db.get_engine()
    sql = text('SELECT DISTINCT Night_Of FROM sleep_data ORDER BY Night_Of')
    with engine.connect() as conn:
        result = conn.execute(sql)

        aggregator = sleep_maths.Aggregator()

        for night_row in result:
            night = night_row.night_of
            session = sleep_session.SleepSession(night)
            retriever = night_retriever.NightRetriever(conn, night)

            summary_repo = session_summary.SummaryRepository(conn)

            for row in retriever.fetch_sleep_records():
                record = sleep_record.SleepRecordFactory.create_sleep_record(row)
                session.add_record(record)

            # So now /session/ has all the records for the /night/ we want to create a summary
            summary = session_summary.SessionSummaryFactory.create_session_summary(session)

            # then you want to do whatever maths you need to
            summary.calculate_averages(aggregator)

            # # and finally you want to store it
            summary_repo.persist_summary(summary)
