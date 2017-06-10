from wombat import models
from wombat import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect, desc, exists

engine = create_engine(settings.DATABASE_URI, echo=True)
session = sessionmaker(bind=engine)
Session = session()

#this next line creates the database if it doesn't exists already
models.Item.metadata.create_all(engine)
