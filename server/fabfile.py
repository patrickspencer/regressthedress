from fabric.api import *
import configparser

config = configparser.RawConfigParser()
config.read('server_settings.ini')

env.hosts = [config.get('env', 'hosts')]
env.user  = config.get('env', 'user')

def gitpull():
    with cd("/var/styelend"):
        run('git pull')

def collectstatic():
    with cd("/var/stylelend"):
        run('python manage.py collectstatic')
