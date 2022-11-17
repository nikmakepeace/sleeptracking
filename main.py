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
    pass