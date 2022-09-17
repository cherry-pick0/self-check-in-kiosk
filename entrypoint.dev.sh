# Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
#!/bin/sh

# Verify that Postgres is healthy before applying the migrations
# and running the Django development server

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
