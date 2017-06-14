#!/bin/bash

NAME="wombat"                                 # Name of the application
PROJECT_DIR=/home/ubuntu/wombat/wombat/                   # Project directory
SOCKFILE=/home/ubuntu/wombat/okapi_gunicorn.sock  # we will communicate using this unix socket
LOGFILE=/home/ubuntu/wombat/wombat_logs/wombat_gunicorn.log		         # we will communicte using this unix socket
USER=ubuntu                         # the user to run as
GROUP=webapps                                    # the group to run as
NUM_WORKERS=3                                    # how many worker processes should Gunicorn spawn
WSGI_MODULE=wombat.webapp.wsgi:app                          # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $PROJECT_DIR
. /home/ubuntu/wombat/.virtualenvs/wombat/bin/activate
source /home/ubuntu/wombat/.virtualenvs/wombat/bin/postactivate
export PYTHONPATH=$PROJECT_DIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ubuntu/wombat/.virtualenvs/wombat/bin/gunicorn ${WSGI_MODULE} \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --reload
