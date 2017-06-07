import pandas as pd
import numpy as np

## 'engine' is a connection to a database
## Here, we're using postgres, but sqlalchemy can connect to other things too.
# engine = create_engine('postgres://%s@localhost/%s'%(username,dbname))
# print engine.url

df = pd.DataFrame.from_csv('Crunchbase_Startup_Investment_Data.csv', encoding='latin1')

