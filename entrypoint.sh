#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn td_mvp.wsgi:application --bind 0.0.0.0:8000