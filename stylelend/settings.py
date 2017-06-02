import pytz
import os

DATABASE = {
        'NAME': "stylelend",
        'USER': "patrick",
        "PASSWORD": "pass",
        "HOST": "localhost",
        "PORT": "5432",
    }

LOCAL_TIMEZONE = 'US/Eastern'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# DATABASE_URI = "sqlite:///%s" % os.path.join(BASE_PATH,'db.sqlite3')
DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (DATABASE['USER'],
        DATABASE['PASSWORD'],DATABASE['HOST'],DATABASE['PORT'],DATABASE['NAME'])
