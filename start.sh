#!/bin/sh

sleep 10

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages

gunicorn --bind 0.0.0.0:8000 hikingapp.wsgi --timeout 0
