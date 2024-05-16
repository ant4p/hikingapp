#!/bin/sh

sleep 5

apt install gettext

sleep 15

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages

gunicorn --bind 0.0.0.0:8000 hikingapp.wsgi --timeout 0
