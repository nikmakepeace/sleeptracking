from datetime import timedelta

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
import orm_setup
Base = orm_setup.Base


class SleepRecord(Base):
    """A single record from a sleep monitor"""
    __tablename__ = "sleep_data"
    id = Column(Integer, primary_key=True)
    dt = Column(DateTime, nullable=False)
    spo2 = Column(Integer, nullable=False)
    pulse_rate = Column(Integer, nullable=False)
    motion = Column(Integer, nullable=False)
    spo2_reminder = Column(Boolean, nullable=False)
    pr_reminder = Column(Boolean, nullable=False)
    session_id = Column(Integer, ForeignKey('sleep_state.id'))

    sleep_session = relationship('SleepSession', back_populates='sleep_records')

    def __repr__(self):
        return f"SleepRecord(id={self.id!r}, dt={self.dt!r}, spo2={self.spo2!r}, pulse_rate={self.pulse_rate!r}, \
            motion={self.motion!r}, spo2_reminder={self.spo2_reminder!r}, pr_reminder={self.pr_reminder!r}, \
            night_of={self.night_of!r} "

    def calculate_night_of(self):
        # determine which night's sleep this is (assume if its before 3PM it belongs to the night before)
        # probably doesn't belong here
        this_day = self.dt
        if self.dt.hour < 15:
            night_of = this_day - timedelta(days=1)
        else:
            night_of = this_day

        return night_of.date()
