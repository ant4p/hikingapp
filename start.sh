#!/bin/sh

until python manage.py migrate
do
    echo "Database preparation..."
    sleep 5

done
python manage.py collectstatic --noinput
python manage.py compilemessages

gunicorn --bind 0.0.0.0:8000 hikingapp.wsgi
