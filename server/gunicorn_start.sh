#!/bin/bash

NAME="okapi_app"                                    # Name of the application
DJANGODIR=/home/ubuntu/okapi                        # Django project directory
SOCKFILE=/home/ubuntu/okapi_gunicorn.sock           # we will communicate using this unix socket
LOGFILE=/home/ubuntu/okapi_logs/okapi_gunicorn.log  # we will communicte using this unix socket
USER=ubuntu                                         # the user to run as
GROUP=webapps                                       # the group to run as
NUM_WORKERS=3                                       # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.production   # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi                      # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/ubuntu/.virtualenvs/okapi/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ubuntu/.local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGFILE
  --reload
