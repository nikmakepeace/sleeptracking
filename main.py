from sqlalchemy import create_engine, run_sql
import SleepSession
import SessionSummary
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

    # Get instances of the basically static factories, maths, and storers
    summary_factory = SessionSummary.SessionSummaryFactory()
    summary_storer = SessionSummary.SummaryRepository(engine)
    record_factory = SleepRecord.SleepRecordFactory()
    aggregator = SleepMaths.Aggregator()

    for night in nights:
        retriever = NightRetriever.NightRetriever(engine, night)
        session = SleepSession.SleepSession(night)

        sleep_rows = retriever.fetch_sleep_records()

        for row in sleep_rows:
            record = record_factory.create_sleep_record(row)
            session.add_record(record)

        # So now /session/ has all the records for the /night/ we want to create a summary
        summary = summary_factory.create_session_summary(session)

        # then you want to do whatever maths you need to
        summary.calculate_averages(aggregator)
        print(summary.mean_pr)

        # and finally you want to store it
        summary_storer.persist_summary(summary)
