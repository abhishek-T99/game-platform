#!/bin/sh
export DJANGO_SETTINGS_MODULE=hello.settings
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec opentelemetry-instrument \
  gunicorn hello.wsgi:application \
  --bind 0.0.0.0:8000