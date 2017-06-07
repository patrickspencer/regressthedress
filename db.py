import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "patrick"
DB_PASS = "pass"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "stylelend"

DB_URI = 'postgres://%s:%s@%s:%s/%s' % (
	 DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

engine = create_engine(DB_URI, echo=True)
session = sessionmaker(bind=engine)
Session = session()

# rentals = pd.DataFrame.from_csv('style_lend_all_rentals.csv')
# rental_items = pd.DataFrame.from_csv('style_lend_all_rentals_items.csv')
items = pd.DataFrame.from_csv('style_lend_all_items.csv')
# rentals.to_sql('rentals', engine, if_exists='replace')
# rental_items.to_sql('rental_items', engine, if_exists='replace')
items.to_sql('items', engine, if_exists='replace')


