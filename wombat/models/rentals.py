from wombat.models import dbsession
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Float

Base = declarative_base()


class Rental(Base):
    __tablename__ = 'rentals'

    id                = Column(Integer, primary_key=True)
    total_cost        = Column(Float)
    created_at        = Column(DateTime)

    def __repr__(self):
       return "<Rental(total_cost='%s', created_at='%s')>" \
               % (self.total_cost, self.created_at)
