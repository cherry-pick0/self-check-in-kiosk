# Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

###########
# BUILDER #
###########

# Base image
## This installs a Python image into the Docker image.
## This is also the version of Python that will run the application in the container
FROM python:3.9.6-alpine as builder

# Set work directory
## This will be the root directory of the Django app in the container
# Where your code lives
## This explicitly tells Docker to set the provided directory as
## the location where the application will reside within the container
WORKDIR /usr/src/kiosk

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# lint
#RUN pip install --upgrade pip
#RUN pip install flake8==3.9.2
#COPY . .
#RUN flake8 --ignore=E501,F401 .

# Install dependencies
RUN pip install pipenv
# Note: why not pipenv install?
# Workaround for requirements.txt
COPY Pipfile /tmp
COPY Pipfile.lock /tmp
RUN cd /tmp && pipenv requirements > requirements.txt

RUN cd ../
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/kiosk/wheels -r /tmp/requirements.txt



#########
# FINAL #
#########

# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/kiosk/wheels /wheels
COPY --from=builder /tmp/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# Copy whole project to your docker home directory.
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
# todo is this the right file path?
ENTRYPOINT ["./entrypoint.prod.sh"]
