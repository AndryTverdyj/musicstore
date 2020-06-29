#!/bin/bash

set -e
python3 manage.py makemigrations --no-input
python3 manage.py migrate
python3 manage.py collectstatic --no-input
gunicorn --env DJANGO_SETTINGS_MODULE=app.settings -b 0.0.0.0:8000 -w 4 app.wsgi &
wait -n
