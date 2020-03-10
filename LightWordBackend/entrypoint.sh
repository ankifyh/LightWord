#!/bin/sh

while ! nc -z db 3306; do sleep 3; done

echo "App can connect db!"

while ! nc -z redis 6379; do sleep 3; done

echo "App can connect redis!"

/usr/local/bin/gunicorn -c config/gunicorn.py lightword:app --log-config config/logging.conf