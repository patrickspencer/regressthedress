"""
    models
    ~~~~~~
    Model definitions and class methods
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from stylelend import settings

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
dbsession = Session()

from stylelend.models.items import *
from stylelend.models.rentalitems import *
