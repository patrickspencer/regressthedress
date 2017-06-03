import datetime
from stylelend.models import dbsession
from stylelend.models.items import Item
from stylelend.models.rentals import Rental
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Float

Base = declarative_base()


class RentalItem(Base):
    __tablename__ = 'rental_items'

    id                = Column(Integer, primary_key=True)
    item_id           = Column(Integer, ForeignKey(Item.id))
    rental_id         = Column(Integer, ForeignKey(Rental.id))
    item_price        = Column(Float)

    def __repr__(self):
       return "<RentalItem(item_id='%s')>" % (self.item_id)
