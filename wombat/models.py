"""
    models
    ~~~~~~
    Model definitions and class methods
"""

from wombat import settings
from sqlalchemy import create_engine
from sqlalchemy import Table, exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Boolean, Float

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
dbsession = Session()


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
    location          = Column(String)
    rental            = relationship("RentalItem")

    def __repr__(self):
       return "<Item(title='%s', brand='%s', type='%s')>" \
               % (self.title, self.brand, self.item_type)


class RentalItem(Base):
    __tablename__ = 'rental_items'

    id         = Column(Integer, primary_key=True)
    item_id    = Column(Integer, ForeignKey(Item.id))
    item_price = Column(Float)

    def __repr__(self):
       return "<RentalItem(item_id='%s', price='%s')>" % (self.item_id, self.item_price)

class Rental(Base):
    __tablename__ = 'rentals'

    id                = Column(Integer, primary_key=True)
    total_cost        = Column(Float)
    created_at        = Column(DateTime)

    def __repr__(self):
       return "<Rental(total_cost='%s', created_at='%s')>" \
               % (self.total_cost, self.created_at)

class ItemAdjective(Base):
    __tablename__ = 'item_adjectives'

    id                = Column(Integer, primary_key=True)
    name              = Column(String)

class ItemType(Base):
    __tablename__ = 'item_types'

    id                = Column(Integer, primary_key=True)
    name              = Column(String)

class ItemBrand(Base):
    __tablename__ = 'item_brands'

    id                = Column(Integer, primary_key=True)
    name              = Column(String)
