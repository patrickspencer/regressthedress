import os
import socket
import random
import configparser
from pathlib import Path

config = configparser.RawConfigParser()

config_file_str = "/etc/okapi_production_settings.ini"
config_file = Path(config_file_str)

def create_secret_key():
    ascii_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join([random.SystemRandom().choice(ascii_chars) for i in range(50)])

def make_config_file():
    if not config_file.is_file():
        print("/etc/okapi_production_settings.ini does not exist. Making new one.")
        config['secrets'] = {}
        config['secrets']['SECRET_KEY'] = create_secret_key()

        config['database'] = {}
        config['database']['DATABASE_NAME'] = ''
        config['database']['DATABASE_USER'] = ''
        config['database']['DATABASE_PASSWORD'] = ''
        config['database']['DATABASE_PORT'] = ''

        config['general'] = {}
        config['general']['DEBUG'] = ''
        config['general']['ALLOWED_HOSTS'] = ''
        with open(config_file_str, 'w') as configfile:
            config.write(configfile)
            print("Wrote new config file template at /etc/okapi_production_settings.ini")
    else:
        print("/etc/okapi_production_settings.conf file already exists")
        exit()

if __name__ == '__main__':
    make_config_file()
