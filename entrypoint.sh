#!/bin/sh

if [ "$SQL_ENGINE" = "django.db.backends.mysql" ]
then
    echo "Waiting for database..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "SQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"