"""
    models
    ~~~~~~
    Model definitions and class methods
"""

from wombat.webapp import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
dbsession = Session()

from wombat.models.items import *
from wombat.models.rentalitems import *
