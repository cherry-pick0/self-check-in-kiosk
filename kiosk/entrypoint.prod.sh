#!/bin/sh
# Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
# Verify that Postgres is healthy before applying the migrations...


if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"
