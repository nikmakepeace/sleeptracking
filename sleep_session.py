from sleep_maths import Aggregator
from sleep_record import SleepRecord
from sqlalchemy import Column, Integer, Date, Float
from sqlalchemy.orm import relationship

import orm_setup
Base = orm_setup.Base


class SleepSession(Base):
    """Represents the summary of a sleep session. Created from SleepSession data"""
    __tablename__ = 'sleep_state'
    id = Column(Integer, primary_key=True)
    night_of = Column(Date, nullable=False, unique=True)
    mean_spo2 = Column(Float, nullable=True)
    mean_pr = Column(Float, nullable=True)

    sleep_records = relationship('SleepRecord', order_by=SleepRecord.id, back_populates='sleep_session')

    def calculate_averages(self, aggregator: Aggregator):
        self._calculate_mean_spo2(aggregator)
        self._calculate_mean_pr(aggregator)

    def _calculate_mean_spo2(self, aggregator: Aggregator):
        spo2_records = []
        for record in self.sleep_records:
            spo2_records.append(record.spo2)
        self.mean_spo2 = aggregator.mean(spo2_records)

    def _calculate_mean_pr(self, aggregator: Aggregator):
        pr_records = []
        for record in self.sleep_records:
            pr_records.append(record.pulse_rate)
        self.mean_pr = aggregator.mean(pr_records)
