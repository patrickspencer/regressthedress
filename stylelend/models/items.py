import datetime
from stylelend.models import dbsession
from sqlalchemy.orm import relationship
from sqlalchemy import exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Boolean, Float

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id                = Column(Integer, primary_key=True)
    item_type         = Column(String)
    size              = Column(Integer)
    title             = Column(String)
    description       = Column(String)
    brand             = Column(String)
    cost              = Column(Float)
    rent_per_week     = Column(Integer)
    groupings         = Column(String)
    user_id           = Column(Integer)
    city              = Column(String)
    state             = Column(String)
    datetime          = Column(DateTime(timezone=True))
    location          = Column(String)

    def __repr__(self):
       return "<Item(name='%s')>" % (self.title)
