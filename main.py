from sqlalchemy import create_engine, run_sql
import SleepSession
import SleepMaths
import NightRetriever
import SleepRecord

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

    engine = create_engine('mysql://hennigan:niknoseepwd@localhost/sleep_study_database')
    nights = run_sql('SELECT DISTINCT Night_Of FROM sleep_state ORDER BY Night_Of', engine)

    for night in nights:
        retriever = NightRetriever.NightRetriever(engine, night)
        session = SleepSession.SleepSession(night)
        record_factory = SleepRecord.SleepRecordFactory()

        sleep_rows = retriever.fetch_sleep_records()

        for row in sleep_rows:
            record = record_factory.create_sleep_record(row)
            sess

