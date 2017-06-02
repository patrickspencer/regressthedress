import datetime
from stylelend.models import dbsession
from stylelend.models.items import Item
from sqlalchemy.orm import relationship
from sqlalchemy import exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, ForeignKey, Boolean, Float

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id                = Column(Integer, primary_key=True)
    item_id           = Column(Integer, ForeignKey(Item.id))
    item_price        = Column(Float)

    def __repr__(self):
       return "<Item(name='%s')>" % (self.title)
