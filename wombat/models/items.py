import datetime
from wombat.models import dbsession
from sqlalchemy import Table, exists
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Boolean, Float

Base = declarative_base()

association_table = Table('rental_items', Base.metadata,
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('rental_id', Integer, ForeignKey('rental.id'))
)


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
    location          = Column(String)

    def __repr__(self):
       return "<Item(title='%s', brand='%s', type='%s')>" \
               % (self.title, self.brand, self.item_type)
